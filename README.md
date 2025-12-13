# Mapping the Potential Destructive Power of Wildfires Using Machine Learning
*Version 4.0*

Author: Dustin Littlefield\
Project Type: Data Science & GIS Portfolio\
Technologies: ArcGIS, Python, Pandas, Scikit-learn, XGBoost, GeoPandas, Matplotlib\
Skills: `Data cleaning` `feature engineering` `supervised machine learning` `model evaluation` `class imbalance handling` \
`spatial visualization` `exploratory data analysis` `reproducible workflow design` `results communication`\
Status: In Progress\
Last Updated: December 2025\
[Github Repository](https://github.com/dustinlit/California_Fire_Severity)

**Disclaimer:** I am not a climate scientist or wildfire expert. This project is intended to demonstrate data science, geospatial, and machine learning skills. It is not designed for operational use or policy decisions.

## Overview
This project is a work in progress that explores the relationship between wildfire severity and environmental, geographical, social and temporal factors in the state of California. The goal is to predict a custom severity index `Wildfire Potential Destructive Power` — which incorporates structures damaged, structures destroyed and acres burned as degrees of fire severity.

## Objectives
- Predict wildfire damage potential based on environmental, geographical and social data.
- Extrapolate statewide wildfire coverage by integrating daily weather data and fire records through spatial analysis of a mesh network of buffered points across California.
- Compare several multi-classification modelling techniques including `XGBoost`,`Random Forest`, and a `Neural Network`.
- Compare class balancing techniques between `RandomUnderSampler`, `SMOTE`, and unbalanced and measure thier effect on model performance.
- Utilize interpolation techniques to create geospatial visualizations that illustrate local and regional risk patterns.
- Explore relationships between key factors with wilfire severity and model importance.

## Key Initial Insights:
- In the mesh network, there were a total of **57,203** incidents of wildfires detected between 01/01/2018 and 12/31/2024 thoughout the state.
- **13,925** of these were *high* risk incidents causing significant property damage or acreage burned.
- Wildfire events appear to be increasing over time. `Year` is a strong contributor to the models.
- Human factors weigh heavily in the models, `Population` and `Housing` density contribute substantially to the random forest model (the best performer).
- Regional factors like `WUI interface` and `WUI intermix` zones contribute reasonably as well.
- Surprising to me, weather factors alone are poor predictors of fire severity.
- `Tree` based models appear to capture the complicated relationships best.

<img src="plots/RF_top.png" alt="Model Metrics for Case Study" width="400" style="display: block; margin-left: 0;" />

<img src="data/maps/interpolation.jpg" width="1200">

## Initial Challenges
- **Dataset size** - The addition of higher granularity and additional data is leading to ***prohibitively large and unwieldy processor times*** on current hardware. It has become a balancing act to trim the dataset for efficient workflow without overly affecting model performance.
- **Heavy Class Imbalance** - Damaging wildfire events are rare compared to days with no significant events. The low risk class is composed of $389,137$ data points compared to the $13,925$ members of the high risk class. `Undersampling` the majority class works best for balancing, while oversampling tends to ***add too much noise*** to the models.
- **Messy Real World Data** - Data with large gaps, data without handy relevant spatial fields, data in which you have to wrangle random mistakes. Some days feel like a rodeo, so many promising avenues become dead ends due to the potential time sink.
### Version 4.0 Changelog
> 1. New Datasets
>     - Detailed Elevation data (slope,aspect, northness, eastness)
>     - Infrastructure data (roads, power lines)
>     - Land Cover data
> 2. Refined ArcGIS worklow
> 3. Changed samples from points to a grid structure to ensure even coverage of the state with minimal overlap.
> 4. Replaced Neural Network with LightGBM tree model

### Version 3.0 Changelog
> 1. Incorporated more accurate and complete raster weather data from **gridMET Climatology Lab**
> 2. Integrated **Wildland Urban Interface** and **California Eco regions**.
> 2. Replaced the `KNN` model with a `Neural Network` for a simpler data workflow.
> 3. ArcGIS Pro integration for data preparation and prediction interpolation
> 4. Added more accurate Census Block data. Population stats calculated as buffer zone around sampling points.


### Version 2.0 Changelog
> 1. Added Detailed fire damage data
>       - CALFIRE damage cost data added, 
>       - Estimation of damage directly from structures
> 2. Expanded the dates for weather and damage data
>       - Expanded from 2018-2020 to 2018-2025
> 3. New Features
>       - `Fire History` average fires per month for previous years
> 4. Data Handling Optimization
>       - Simplified handling of case study data as references instead of storing separate databases
> 5. Geographical and Temporal Integration
>       - in ArcGIS, constructed a mesh sampling grid in California to ensure even coverage
>       - Buffer spatial join for combining fire damage info with weather data
>       - Incorporated Regionality and Seasonality into models


<img src="plots/wildfires.png" width="600">

## Project Structure

California_Fire_Severity/\
├── data/\
├── notebooks/\
│ ├── 01_Data_Exploration_Processing.ipynb\
│ ├── 02_Data_Merging.ipynb\
│ ├── 03_Feature_Engineering.ipynb\
│ ├── 04_Variable_Selection.ipynb\
│ ├── 05_Feature_Interaction_Analysis.ipynb\
│ ├── 06_Class_Balancing.ipynb\
│ ├── 07_Modeling_and_Tuning.ipynb\
│ ├── 08_Evaluation_and_Visualization.ipynb\
│ ├── A_Appendix_Sampling_Points.ipynb\
│ ├── B_Appendix_Wildfires.ipynb\
│ ├── C_Appendix_Gridmet_Combination.ipynb\
│ ├── D_Appendix_Gridmet_Extraction.ipynb\
├── plots/\
│ ├── Palisades_predictions.png\
│ ├── Interpolated.png\
│ ├── sampling_metrics.png\
│ └── file_structure.png\
├── src/\
├── Optimizing_Emergency_Response.pdf\
├── README.ipynb\
└── README.md

### Data Sources

> **Fire Incident Data**:
 - **Wildfire damage data**: *CAL FIRE Damage Inspection (DINS)* <https://data.ca.gov/dataset/cal-fire-damage-inspection-dins-data>'
 - **Wildfire incidents**: *Calfire Incidents* <https://www.fire.ca.gov/incidents>

> **Environmental Data**:
 - **Daily weather readings**: *gridMET* <https://www.climatologylab.org/gridmet.html>

> **California Demographic Data** :
 - **Census Tract Data**: *U.S. Census Bureau, Department of Commerce* <https://catalog.data.gov/dataset/tiger-line-shapefile-2021-state-california-census-tracts>
 - **2024 American Community Survey 5 year Median Income Data** *U.S. Census Bureau, Department of Commerce* <https://data.census.gov/table/ACSST1Y2024.S1903?q=California+Income&g=010XX00US$1500000_040XX00US06$1400000,06$1500000>
> **Wildlife Urban Interface**: 
- **WUI layer**: *California Department of Forestry and Fire Protection* <https://gis.data.ca.gov/datasets/CALFIRE-Forestry::wildland-urban-interface/explore?location=34.403601%2C-118.894358%2C9.95>
- **CDFW regions**: *California Department of Fish and Wildlife* <https://data.ca.gov/dataset/cdfw-regions>
- **Eco Regions** - *USDA Forestry Service*
<https://data.fs.usda.gov/geodata/edw/datasets.php?dsetCategory=biota>

**Raw Data Processed in:**
> - *notebooks/A_Appendix_Sampling_Points.ipynb*
> - *notebooks/B_Appendix_Wildfires.ipynb*
> - *notebooks/C_Appendix_Gridmet_Combination.pynb*
> - *notebooks/D_Appendix_Gridmet_Extraction.pynb*

## Key Factors:
Environmental / Weather Variables:
- `Air Temperature`-	Daily aximum and minimum air temperature at 2 meters above ground (Kelvin)
- `Vapor Pressure Deficit` - kPa Difference between saturation vapor pressure and actual vapor pressure (kPa); indicates atmospheric drying power
- `Relative Humidity`	-Maximum daily relative humidity (%) at 2 meters
- `Wind Speed` - Daily wind speed (m/s) at 10 meters
- `Actual Evapotranspiration`	- Estimated evapotranspiration from actual vegetation (mm/day)
- `Palmer Drought Severity Index`	- Long-term drought index combining temperature and precipitation to measure dryness
- `Standardized Precipitation Index` - Short-term precipitation deficit; captures recent drying of fine fuels

Fire Danger Indicators:
- `Burning_Index`	- Fire danger index derived from temperature, humidity, wind, and fuel moisture; higher values indicate higher fire potential
- `Energy_Release_Component` - Estimated energy release per unit area (MJ/m²); relates to potential fire intensity
- `Dead_Fuel_Moisture` - Moisture content of medium-size dead fuels (%) affecting fire spread

Temporal Variables:
 - `Season`,`Month`,`Year`

Sampling Grid Data:
- `Interface`, `Intermix`, and `Influence` Areas - From WUI, average area of each zone within 36KM Buffer radius around sampling points
- `Total_Population`,`Population_Density`,`Total_Housing`,`Housing_Density` - Population and housing statistics within 36KM Buffer radius around sampling points
- `Eco_Regions` - regions generally representing the varied climate and vegetative regions in California
- `Slope`,`Aspect` Derived from high resolution USGS daily rasters 
- `Land Cover` Derived from land cover raster
- `Roads`,`Power Lines`
#### **ArcGIS Mesh Network:**

<img src="../data/maps/grids.png" width="400">

## Feature Engineering
*Located in:* 
> - *notebooks/03_Feature_Engineering.ipynb*
> - *notebooks/04_Variable_Selection.ipynb*

Engineered Data: 
- `Average_Fires_per_Month` - Historical 2 year rolling average count of fires per county
- `7-day_Lagged_Weather` - rolling 7 day average for key weather variables

## Class Balancing (Updating)
*Located in:* 
> - *notebooks/06_Class_Balancing.ipynb*

**Target:** *Wildlife Potential Destructive Power* - categorized into Low (0), Moderate(1), High(1)

**Issues:** Moderate and High Damage wildfire events classes are underrepresented.

Balancing Techniques Used:
- In method class balancing
- Random UnderSampler for the dominant "Low" class.
- SMOTE for oversampling

Automatic comparison and selection of class balancing strategies.

<img src="plots/class_balance_v3.png" alt="Model Results" width="400" style="display: block; margin-left: 0;" />

## Modeling
*Located in:*
> - *notebooks/07_modeling_And_Tuning.ipynb*

Models are tuned automatically and the best performing models are selected for final evaluation and visualization.

**Models tested:**
- `Random Forest` from scikit-learn
- `Light GBM` from scikit-learn
- `XGBoost` from XGBoost

**Metrics evaluated:**
`F1-score (macro-averaged)`
`Confusion matrices`
`Cross-validation`

Feature importance extracted for tree-based models.

## Model Metrics

**Key Findings:** 
- All Models struggle with distinguishing **Moderate** from **High** severity classes.
- Tree models performed comparably, may need further tuning
- Neural Network currently struggles

### Metrics for real world case study: `Palisades Fire` - 01/07/2025: (Updating)

<img src="plots/Metrics.png" alt="Model Metrics for Case Study" width="500" style="display: block; margin-left: 0;" />

## **Feature Importances** for Tree models: (Updating)

<img src="plots/RF_top.png" alt="Model Metrics for Case Study" width="400" style="display: block; margin-left: 0;" />


<img src="plots/XGB_top.png" alt="Model Metrics for Case Study" width="320" style="display: block; margin-left: 0;" />

## Conclusions:
- `Year` is a leading factor in both tree models. Suggesting that fire severity is increasing, maybe due to climate change.
- Most **weather** Variables rank low on model importance suggesting a more complicated relationship with wildfire severity
- **Population** stats play a key role in prediciting wildfire severity
- More data may be neccessary for better correllations

## Visualization (updating)
*Located in:*
> - *notebooks/08_evaluation_and_visualization.ipynb*

- Maps using GeoPandas, Matplotlib, and Seaborn.
- IDW interpolation for environmental variables in ArcGIS.

Example Python Output:

<img src="plots/results.png" alt="California 01072025" width="1500" style="display: block; margin-left: 0;" />
---

## Challenges

> **Weak Correlation** – Environmental features don’t fully explain severity outcomes.\
> **Class Imbalance** – Damaging fires are rare; balancing was essential.\
> **Limited Processing Power** - Limits the granularity of the sampling mesh and increases modeling time due to larger datasets.\
> **Data Incompatability** - Interpreting some more complex factors like reservoir levels and response times is complicated due to missing and spatially uncorrelated data.

## Next Steps / Potential Improvements
- Hot Spot analysis of daily NDVI raster data (in process)
- Arcpy integration.
- Incorporate emergency response times and reservoir data
- Time series maps to check models consistency over time
- Seperate module for up to date processing of new information and real time predictions
- Consult domain experts to validate assumptions and feature selection.

## Installation
To run the project locally:\
git clone https://github.com/dustinlit/wildfire-severity.git \
cd wildfire-severity\
pip install -r requirements.txt

## License
This project is released under the MIT License.
See LICENSE for details.