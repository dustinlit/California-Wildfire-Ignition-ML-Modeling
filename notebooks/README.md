# Changelog for Version 2

## Changes Made
#### 1. Added Detailed fire damage data
-  CALFIRE damage cost data added
    - Estimate cost of damage from damage to structures
    - More accurate target
    - Attaches significance to fires that cause damage only
    - Expands coverage to 2018-2025
#### 2. Expanded the dates for weather data
- Expanded from 2018-2020 to 2018-2025
#### 3. New Features
- Fire History 
    – average fires per month for previous years
- Dryness indicator
     – rolling count of days without rain
#### 4. Data Handling Optimization
- Simplified handling of case study data as references instead of storing separate databases
#### 5. Geographical and Temporal Integration
- in ArcGIS, constructed a mesh sampling grid in California to ensure even coverage
- Buffer spatial join for combining fire damage info with weather data
- Incorporated Regionality and Seasonality into models
## Upcoming Improvements (in progress)
#### 1. Modeling Response Times
- Incorporate firefighting station location data
- Spatial join firefighting stations within a buffered area from weather stations
#### 2. Regression
- Adding prediction of potential dollar cost instead of categorical threat level
#### 3. More ArcGIS pro integration for better visualization
#### 4. Additional Features
- Drought indicator – Potential Evapotranspiration (PET_proxy)
    - PET_proxy = a * Temp_mean + b * Wind Speed + c * SolarRadiation - d * Humidity

