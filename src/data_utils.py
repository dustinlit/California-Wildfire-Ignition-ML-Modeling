import pandas as pd
import numpy as np
from itertools import combinations
from shapely.geometry import Point, Polygon

def rank_variables_by_correlation(df, target_series):

    correlations = df.corrwith(target_series)
    correlation_df = correlations.reset_index()
    correlation_df.columns = ['Feature', 'Correlation']
    correlation_df = correlation_df.sort_values(by='Correlation', key=abs, ascending=False).reset_index(drop=True)
    return correlation_df

def create_2nd_degree_interactions(df):

    numeric_cols = df.select_dtypes(include='number').columns
    interactions = {}

    for col1, col2 in combinations(numeric_cols, 2):
        interaction_name = f"{col1} x {col2}"
        interactions[interaction_name] = df[col1] * df[col2]

    return pd.DataFrame(interactions, index=df.index)

def create_interactions(df, degrees=[2, 3]):

    numeric_cols = df.select_dtypes(include='number').columns
    interactions = {}

    for degree in degrees:
        for combo in combinations(numeric_cols, degree):
            interaction_name = " x ".join(combo)
            product = df[list(combo)].prod(axis=1)  # multiply all columns in the combo
            interactions[interaction_name] = product

    return pd.DataFrame(interactions, index=df.index)

def basic_explore(df):
    print('Rows: ', df.shape[0], ' Columns: ', df.shape[1])
    print('Duplicates ', df.duplicated().sum())
    datapoints = df.shape[0] * df.shape[1]
    print('Total NA values: ', df.isna().sum().sum(), ' of ', datapoints, 'datapoints')

def post_merge_check (merged_df, premerged_df, keys=False):
    
    if keys:
        print("Duplicate Keys: ", merged_df[keys].duplicated().sum()) 
    print("Premerged shape: ", premerged_df.shape)
    print("Merged shape: ", merged_df.shape)
    print("Duplicates before merge: ", premerged_df.duplicated().sum())
    print("Duplicates after merge: ", merged_df.duplicated().sum())
    print('NA values before merge: ', premerged_df.isna().sum().sum())    
    print('NA values after merge: ', merged_df.isna().sum().sum())    
    
def square_buffer(point, size):

    #Create a square Polygon centered on a Point
    #size: half the side length
        
    x, y = point.x, point.y
    
    return Polygon([
        (x - size, y - size),
        (x - size, y + size),
        (x + size, y + size),
        (x + size, y - size)
    ])
