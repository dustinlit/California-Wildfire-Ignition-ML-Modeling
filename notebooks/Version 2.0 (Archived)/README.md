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
> - `Slope and Aspect` South Facing Slopes
> - LANDFIRE - https://landfire.gov/data
> - `Time since last fire`
>- California State Responsibility Areas https://gis.data.ca.gov/maps/5ac1dae3cb2544629a845d9a19e83991/about
> - More Detailed `Census Block or Tract Data`
