## Changelog for Version 2

#### Added Detailed fire damage data
-  CALFIRE structural damage data added
    - Estimate cost of damage from damage to structures
    - More accurate target
    - Attaches significance to fires that cause damage only
#### Expanded the dates for fire damage and weather data
- Expanded from 2018-2020 to 2018-2024
#### New Features
- Fire History 
    – average fires per month for previous years
- Dryness indicator
     – rolling count of days without rain
#### Data Handling Optimization
- Simplified handling of case study data as references instead of storing separate databases
#### Geographical Integration
- Spatial Join to combine station locations with fire locations

## Upcoming Improvements in progress
####	Incorporate temporality and regionality
#### Modeling Response Times
- Incorporate fire station location data
- Spatial join stations within a buffered area from weather stations
#### Regression
- Adding model a predicted dollar cost instead of a categorical threat level
#### ArcGIS pro integration for better visualization
#### Additional Features
- Drought indicator – Potential Evapotranspiration (PET_proxy)
    - PET_proxy = a * Temp_mean + b * Wind Speed + c * SolarRadiation - d * Humidity

