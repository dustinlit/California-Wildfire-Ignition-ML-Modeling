# Mapping the Potential Destructive Power of Wildfires Using Machine Learning
*Version 2.0*

Author: Dustin Littlefield\
Project Type: Data Science & GIS Portfolio\
Technologies: ArcGIS, Python, Pandas, Scikit-learn, XGBoost, GeoPandas, Matplotlib\
Skills: `Data cleaning` `feature engineering` `supervised machine learning` `model evaluation` `class imbalance handling` `Geospatial Analysis` \
`spatial visualization` `exploratory data analysis` `reproducible workflow design` `results communication`\
Status: In Progress\
Last Updated: November 2025\
[Github Repository](https://github.com/dustinlit/California_Fire_Severity)

## Overview

This project is a work in progress that explores the relationship between environmental weather-related factors and the degree of damage caused by wildfires in California. The goal is to predict a custom severity index `Wildfire Potential Destructive Power`, which incorporates structures damaged and destroyed.

> ## **Disclaimer:** 
> - **This is a *work in progress* for training purposes only. Results do not currently reflect reality or claim to. Any results are unvalidated.**
> - **I am not a climate scientist or wildfire expert. This project is intended to demonstrate data science, geospatial, and machine learning skills. It is not designed for operational use or policy decisions.**

> ### Version 2.0 Features
> 1. Added Detailed fire damage data
>       - CALFIRE damage cost data added
>       - Estimate cost of damage from damage to structures
>       - More accurate target
>       - Attaches significance to fires that cause damage only
> 2. Expanded the dates for weather and damage data
>       - Expanded from 2018-2020 to 2018-2025
> 3. New Features
>       - `Fire History` average fires per month for previous years
>       - `Dryness Indicator` rolling count of days without rain
> 4. Data Handling Optimization
>       - Simplified handling of case study data as references instead of storing separate databases
> 5. Geographical and Temporal Integration
>       - in ArcGIS, constructed a mesh sampling grid in California to ensure even coverage
>       - Buffer spatial join for combining fire damage info with weather data
>       - Incorporated Regionality and Seasonality into models

## Objectives
- Predict wildfire damage potential based on environmental, geographical and social data.
- Test classification models using resampling techniques to handle class imbalance.
- Create geospatial *interpolation visualizations* to illustrate regional risk patterns.
- Explore second-degree feature interactions and correlation to improve model features.

---

### Example Results:

<p align="center">
  <img src="data/maps/IDW_RF.jpg" width="600">
</p>
</b>

<img src="plots/Palisades_predictions.png" width="1000">

## Project Structure

California_Fire_Severity/\
├── data/\
├── notebooks/\
│ ├── 01_Fire_Damage_Processing.ipynb\
│ ├── 02_Weather_Data_Processing.ipynb\
│ ├── 03_Feature_Engineering.ipynb\
│ ├── 04_Variable_Selection.ipynb\
│ ├── 05_Feature_Interaction_Analysis.ipynb\
│ ├── 06_Class_Balancing.ipynb\
│ ├── 07_Modeling_and_Tuning.ipynb\
│ ├── 08_Evaluation_and_Visualization.ipynb\
│ ├── A_Appendix.ipynb\
├── plots/\
│ ├── Palisades_predictions.png\
│ ├── Interpolated.png\
│ ├── sampling_metrics.png\
│ └── file_structure.png\
├── src/\
├── Optimizing_Emergency_Response.pdf\
├── README.ipynb\
└── README.md

---

### Data Sources

**[CAL FIRE Incident Data](https://www.fire.ca.gov/incidents)** – Detailed information on structures damaged or destroyed separated per wildfire event. \
**[California CIMIS irrigation stations](https://cimis.water.ca.gov/)** – Daily weather readings from over a hundred weather stations around California. \
**California Demographic Data** - population and income data obtained from the 2020 US census, used as rough proxy for firefighting resources \
**Various GIS Layers** – Californa state and regional shapefiles to support spatial analysis and visualization.

---

## Data Processing

> - *notebooks/01_Fire_Damage_Processing.ipynb*
> - *notebooks/02_Weather_Data_Processing.ipynb*
> - *notebooks/A_Appendix.pynb*

- Implemented programmatic workflows alongside manual validation to refine and standardize multiple datasets.
- ArcGIS workflow – constructed a systematic lattice of sampling points to optimize spatial coverage.
- Merged detailed fire records with sampling points via an intersect spatial join.
- Imputed missing values as needed for weather readings.

**Environmental / Weather Variables**
- `Avg Air Temp (F)` – represents heat conditions.
- `Avg Vap Pres (mBars)` – Average vapor pressure; indicates atmospheric moisture.
- `Avg Rel Hum (%)` – affects fire ignition and spread.
- `Avg Wind Speed (mph)` – higher speeds can drive fire spread.
- `Precip (in) 7 Day Avg` – Total precipitation in the past 7 days; influences fuel moisture.
- `ETo (in)` – Reference evapotranspiration; approximates water loss from soil and plants.

---

## Feature Engineering

> - *notebooks/03_Feature_Engineering.ipynb*
> - *notebooks/04_Variable_Selection.ipynb*
> - *notebooks/05_Feature_Interaction_Analysis.pynb*

- Created 7-day rolling averages for relevant environmental variables.
- Engineered interaction features and composite indexes.

**Derived / Interaction Features**
- `ETo_x_Vapor_Pressure` – models combined dryness effects.
- `ETo_x_Temp` –  highlights hot, dry conditions.
- `Vapor_Pressure_x_Temp` – Interaction capturing the combined effect of heat and moisture.
- `Vapor_Pressure_x_Wind_Speed` – affects drying conditions.

**Composite Indexes**
- `Days Without Rain` - A simple rolling count roughly estimating drought conditions
- `2 Year Fire History` - Average fires per month in the geographic vicinity in last two years.

---

## Class Balancing
> - *notebooks/06_Class_Balancing.ipynb*

Balancing Techniques explored:
- In-method class balancing
- Manual **undersampling** of the dominant "Low" class.
- SMOTE for **oversampling**

**Issue:** Moderate and High Damage wildfire events are pretty rare so these classes are severely underrepresented in the dataset.

---

## Modeling
> - *notebooks/07_modeling_And_Tuning.ipynb*

**Models tested:**
`Random Forest`
`K-Nearest Neighbors`
`XGBoost`

**Metrics evaluated:**
`F1-score (macro-averaged)`
`Confusion matrices`
`Cross-validation`

Models are tuned automatically and the best performers are selected for the final evaluation and visualization. Additionaly, **feature importance** is extracted for tree-based models.

---

## Visualization
> - *notebooks/08_evaluation_and_visualization.ipynb*

- Mapping and Plotting using ArcGIS, GeoPandas, Matplotlib, and Seaborn.
- Raster data and IDW interpolation created in ArcGIS.

Example Output:

<img src="plots/Interpolated.png" alt="Southern California Wildfire Model Predictions" width="400" style="display: block; margin-left: 0;" />

---

## Key Results

**Key Findings:**
- All Models struggle with distinguishing **Moderate** from **High** severity classes.
- Class balancing improved metrics for minority classes.
- XGBoost is consistently the better performer.

**F1 Scores:**

<img src="plots/class_balance.png" alt="Model Results" width="350" style="display: block; margin-left: 0;" />

---

## Challenges

**Missing Environmental Data** – Gaps in weather readings required imputation.\
**Weak Correlation** – Environmental features don’t fully explain severity outcomes.\
**Damage Threshold** - Division of the moderate and high damage levels\
**Class Imbalance** – Damaging fires are rare; balancing was essential.\
**Derived Variable Uncertainty** – Proxies like Dryness need validation.\
**Spatial Generalization** – Models may not perform well across regions.

---

## Next Steps / Potential Improvements
> - Add vegetative land cover, topography, and WUI datasets.
> - Additional ArcGIS integration.
> - Incorporation of emergency response times
> - Time series maps to check models consistency over time
> - Create module for up to date processing of new readings and real time predictions
> - Consult domain experts to validate assumptions and feature selection.

> ## Ideas
> - Number of `fire stations` in each buffered area
> - Average road distance from fire stations from each point in the buffered region
> - Normalize Total Damage as `Damage per Acre`
> - Refine population density to be in buffered sample areas instead of county
> - Land use layer, more accurate buliding density
> - `WUI` https://gis.data.ca.gov/datasets/CALFIRE-Forestry::wildland-urban-interface/explore?location=34.403601%2C-118.894358%2C9.95
> - Firefighting Facility Locations https://gis.data.ca.gov/datasets/8e72bb9b01954c83bf910cef4174bb3a_0/explore?location=37.091088%2C-119.278900%2C6.50
> - California `Vegetation` https://gis.data.ca.gov/maps/35b4d77128264b3bacd31d9685f974b7/explore?location=36.236024%2C-120.809531%2C13&path=
> - NDVI - Historical Sattelite Data
> - `Slppe and Aspect` South Facing Slopes
> - LANDFIRE - https://landfire.gov/data
> - `Time since last fire`
>- California State Responsibility Areas https://gis.data.ca.gov/maps/5ac1dae3cb2544629a845d9a19e83991/about
> - More Detailed `Census Block or Tract Data`
---

## Installation
To run the project locally:\
git clone https://github.com/dustinlit/wildfire-severity.git \
cd wildfire-severity\
pip install -r requirements.txt

---

## License
This project is released under the MIT License.
See LICENSE for details.