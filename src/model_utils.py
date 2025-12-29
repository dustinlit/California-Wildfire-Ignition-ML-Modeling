# src/eval_utils.py

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMClassifier
from sklearn.model_selection import StratifiedKFold

from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import shap
from sklearn.base import clone

from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE

def gen_report(reports,num_classes = 3):

    classes = []
    
    for i in range(num_classes):
        classes.append(str(i))
    
    metrics = ['precision', 'recall', 'f1-score']

    # Initialize structure: {class: {metric: []}}
    results = {cls: {m: [] for m in metrics} for cls in classes}

    # Collect values
    for report in reports:
        for cls in classes:
            for metric in metrics:
                results[cls][metric].append(report[cls][metric])

    # Compute means
    data = {
        'Category': classes,
        'Precision': [np.mean(results[cls]['precision']) for cls in classes],
        'Recall':    [np.mean(results[cls]['recall']) for cls in classes],
        'F1-Score':  [np.mean(results[cls]['f1-score']) for cls in classes]
    }

    return pd.DataFrame(data)

def kfold(X_train, y_train, model):
        
    report_dicts = []
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    for train_index, test_index in kf.split(X_train):
        X_train_fold, X_test_fold = X_train.iloc[train_index], X_train.iloc[test_index]
        y_train_fold, y_test_fold = y_train.iloc[train_index], y_train.iloc[test_index]

        # Train and predict
        model.fit(X_train_fold, y_train_fold)
        y_pred = model.predict(X_test_fold)

        report = classification_report(y_test_fold, y_pred, output_dict=True)
        report_dicts.append(report)

    return report_dicts

def test_values(model, parameter, value_list, X_train, y_train, parameters, num_classes=5):

    F1_values = []

    # Perform k-fold cross-validation for each value
    for value in value_list:
        if model == 'RF':
            rf_params = parameters['Random Forest']
            rf_params[parameter] = value
            test_model  = RandomForestClassifier(**rf_params)
        elif model == 'XGB':
            xgb_params = parameters['XGBoost']
            xgb_params[parameter] = value
            test_model  = xgb.XGBClassifier(**xgb_params)
                
        reports = kfold(X_train, y_train, test_model)
        Train_metrics = gen_report(reports,num_classes)
        average_f1 = Train_metrics['F1-Score'].sum() / len(Train_metrics['F1-Score'])
        F1_values.append(average_f1)
        print(f"{model}: {parameter} = {test_model.get_params()[parameter]} | Average F1 score = {average_f1:.4f}")

    # identify and save highest F1 score
    optimum_value = value_list[F1_values.index(max(F1_values))]

    x_labels = [str(t) for t in value_list]
    sns.lineplot(x=x_labels, y=F1_values, marker='o')
    #plt.axvline(optimum_value, color='red', linestyle='--', label=f'Best: {optimum_value}')
    best_index = F1_values.index(max(F1_values))
    plt.scatter(x_labels[best_index], F1_values[best_index], color='red', s=100, zorder=5, label=f'Best: {value_list[best_index]}')
    plt.xlabel(parameter)
    plt.ylabel('F1 Score (High Severity)')
    plt.title(model + " " + parameter)
    plt.show()
    
    return optimum_value

def apply_balancing(model, strategies, X, y):
    row = strategies[strategies['Model_Label'] == model]

    if not row.empty:
        best_strategy = row['Best_Strategy'].values[0]
        if best_strategy == 'Oversampling':
            smote = SMOTE()
            X, y = smote.fit_resample(X, y)
        elif best_strategy == 'Undersampling':
            rus = RandomUnderSampler(sampling_strategy='auto', random_state=14)
            X, y = rus.fit_resample(X, y)
    
    return X,y

def evaluate_model(model, X_test, y_test, name="Model"):
    y_pred = model.predict(X_test)
    print(f"Evaluation for {name}")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.3f}")
    print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.3f}")
    print(f"Recall:    {recall_score(y_test, y_pred, average='weighted'):.3f}")
    print(f"F1 Score:  {f1_score(y_test, y_pred, average='weighted'):.3f}")
    print("\n")
    print("---- Classification Report ----")
    print(classification_report(y_test, y_pred))
    print("\n")
    
def get_shap(model,X,y):
    
    X = X.copy()
    y = y.copy()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=14, stratify=y)
    
    model.fit(X_train, y_train)
    
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test, check_additivity=False)
    shap_importance = np.abs(shap_values.values).mean(axis=0)
    shap_dict = dict(zip(X_test.columns, shap_importance))

    shap_max_dict = {k: np.max(v) for k, v in shap_dict.items()}
    top_features = sorted(shap_max_dict.items(), key=lambda x: x[1], reverse=True)
    top_10 = pd.DataFrame(top_features[:10])
    
    return top_10
    
def subset_df(df, target, n_rows):
    
    reduced_df = pd.DataFrame()
    num_classes = len(df[target].unique())
    
    for i in range(num_classes):
        cur_class = df[df[target] == i]
        
        if n_rows <= len(cur_class):
            sampled = cur_class.sample(n=n_rows, random_state=14)
        else:
            sampled = cur_class
        
        reduced_df = pd.concat([reduced_df, sampled], ignore_index=True)
        
    return reduced_df

def gen_report_metric(reports, metric='macro_f1', num_classes = 3):
    
    classes = []
    
    for i in range(num_classes):
        classes.append(str(i))
        
    metrics = ['precision', 'recall', 'f1-score']

    # Initialize structure
    results = {cls: {m: [] for m in metrics} for cls in classes}

    # Collect values
    for report in reports:
        for cls in classes:
            for m in metrics:
                results[cls][m].append(report[cls][m])
                
   # Compute summary metric
    if metric == 'macro_f1':
        macro_f1 = np.mean([np.mean(results[cls]['f1-score']) for cls in classes])
        mf1 = [macro_f1]*len(classes)  # same value for all rows
        
    # Compute mean per class
    data = {
        'Category': classes,
        'Precision': [np.mean(results[cls]['precision']) for cls in classes],
        'Recall':    [np.mean(results[cls]['recall']) for cls in classes],
        'Macro_F1': mf1
    }

    # Compute summary metric
    if metric == 'macro_f1':
        macro_f1 = np.mean([np.mean(results[cls]['f1-score']) for cls in classes])
        data['Macro_F1'] = [macro_f1]*len(classes)  # same value for all rows
    else:
        # placeholder for other metrics if needed
        pass

    return pd.DataFrame(data)

def class_balancing(X_train, y_train, X_test, y_test, model, parameters, sampling_strategy='No_balance', num_classes=5):
    
    if sampling_strategy == 'Undersampling':
        rus = RandomUnderSampler(sampling_strategy='auto', random_state=14)
        X_train, y_train = rus.fit_resample(X_train, y_train)
   
    if sampling_strategy == 'Oversampling':
        smote = SMOTE()
        X_train, y_train = smote.fit_resample(X_train, y_train)
          
    reports = kfold(X_train, y_train, model, parameters, num_classes)    
    Train_metrics = gen_report(reports,num_classes)

    # Retrain on full training set
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    reports = [classification_report(y_test, y_pred, output_dict=True)]
    Test_metrics = gen_report(reports,num_classes)

    # Add context columns
    for df in [Train_metrics, Test_metrics]:
        df['Phase'] = 'Train' if df is Train_metrics else 'Test'
        df['Model'] = model.__class__.__name__
        df['Balancing'] = sampling_strategy

    # Combine and reorder
    combined_metrics = pd.concat([Train_metrics, Test_metrics], axis=0)
    combined_metrics = combined_metrics.reset_index().rename(columns={'index': 'Class'})

    return combined_metrics  

def balancing_subset_df(df, target, n_rows, class0 = .9, class1 = .07, class2 = .03):
    
    reduced_df = pd.DataFrame()
    num_classes = len(df[target].unique())
    
    for i in range(num_classes):
        if i == 0:
            rows = int(n_rows * class0)
            print(rows)
        elif i == 1:
            rows = int(n_rows * class1)
            print(rows)
        else:
            rows = int(n_rows * class2)
            print(rows)
            
        cur_class = df[df[target] == i]
        
        if rows <= len(cur_class):
            sampled = cur_class.sample(n=rows, random_state=14)
        else:
            sampled = cur_class
        
        reduced_df = pd.concat([reduced_df, sampled], ignore_index=True)
        
    return reduced_df

def compare_model(model, X, y, best_strategy, name="Model", test_set = "X"):
    
    X = X.copy()
    y = y.copy() 
    
    X, y = apply_balancing('RF', best_strategy, X, y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=14)
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)  
    report = classification_report(y_test, y_pred, output_dict=True)
    
    results = {
        "Test Set":test_set, 
        "Model": name,
        "Weighted F1": f1_score(y_test, y_pred, average='weighted'), 
        "Macro F1": f1_score(y_test, y_pred, average='macro'),
        "High Risk Recall": report["1"]["recall"],
    }
    
    return results

def kfold_probs(X, y, model):

    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=14)
    
    oof_probs = np.zeros((len(y), 3))
    
    for train_index, test_index in kf.split(X,y):
        
        fold_model = clone(model)
        
        X_train_fold, X_test_fold = X.iloc[train_index], X.iloc[test_index]
        y_train_fold, y_test_fold = y.iloc[train_index], y.iloc[test_index]

        # Train and predict
        fold_model.fit(X_train_fold, y_train_fold)
        probs = fold_model.predict_proba(X_test_fold)
        oof_probs[test_index] = probs

    return oof_probs