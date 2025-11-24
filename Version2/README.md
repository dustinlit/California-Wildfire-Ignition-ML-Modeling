# Changelog for Version 2

## Changes Made
#### 1. Added Detailed fire damage data
-  CALFIRE structural damage data added
    - Estimate cost of damage from damage to structures
    - More accurate target
    - Attaches significance to fires that cause damage only
#### 2. Expanded the dates for fire damage and weather data
- Expanded from 2018-2020 to 2018-2024
#### 3. New Features
- Fire History 
    – average fires per month for previous years
- Dryness indicator
     – rolling count of days without rain
#### 4. Data Handling Optimization
- Simplified handling of case study data as references instead of storing separate databases
#### 5. Geographical Integration
- Spatial Join to combine weather station locations with wildfire locations

## Upcoming Improvements (in progress)
#### 1. Incorporate more temporality and regionality
#### 2. Modeling Response Times
- Incorporate firefighting station location data
- Spatial join firefighting stations within a buffered area from weather stations
#### 3. Regression
- Adding prediction of potential dollar cost instead of categorical threat level
#### 4. ArcGIS pro integration for better visualization
#### 5. Additional Features
- Drought indicator – Potential Evapotranspiration (PET_proxy)
    - PET_proxy = a * Temp_mean + b * Wind Speed + c * SolarRadiation - d * Humidity

