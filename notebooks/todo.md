## 12/06/2025 NOTES

https://www.firescience.gov/ords/prd/jf_jfsp/r/jfspublic/research-search?session=17394184923356

Background
1. Examine the correlation and trend of Vapor pressure deficit and temperature to increasing wildfires. Background articles:
- https://www.drought.gov/news/study-shows-climate-change-main-driver-increasing-fire-weather-western-us

- https://www.pnas.org/doi/10.1073/pnas.1607171113

2. WUI Background: 
- https://vcresearch.berkeley.edu/news/new-model-sheds-light-how-wildfires-spread-through-communities

3. CATASTROPHE MODELS p. 31:
- https://osfm.fire.ca.gov/-/media/osfm-website/committes/wildfire-mitigation-advisory-committee/approved-risk-modeling-report-draft-september-5-2023.pdf

- https://uphelp.org/wp-content/uploads/2025/05/Future-Directions-and-Considerations-05-16-2025.pdf

4. Similar Work: 
- https://www.mdpi.com/2073-4433/12/1/109
- https://hal.science/hal-05240719v1/file/Modelling_California_wildfires_final.pdf

Census Tract Data: https://catalog.data.gov/dataset/tiger-line-shapefile-2021-state-california-census-tracts


ACS 5 year 2023 median income data https://data.census.gov/table/ACSST1Y2024.S1903?q=California+Income&g=010XX00US$1500000_040XX00US06$1400000,06$1500000

Modeling
1. Visualize and explore more feature importance results
2. Fix Neural Network or replace

Presentation
1. executive summary
2. Improve visual polish with consistent color palette, clear legends, and annotated maps/plots.
3. Create a data pipeline diagram showing raw data → features → models → outputs
4. limitations section that clearly states constraints and challenges
5. skills section (e.g., geospatial analysis, class imbalance handling, model interpretability).
6. potential applications (e.g., resource allocation, risk awareness).
7. Add a comparison to literature (brief references to wildfire modeling studies).
8. personal reflection


Expansion IDEA:

- Shrink the model to micro scale - Calculate risk factors of houses known to burn in fires, defensible space, region, aspect, WUI, slope, weather, NDVI and correlate with damage amount undamaged, slightly damaged, destroyed.
- Retrieve sattelite image from day of or before fire
- extract gridMet data at location
- run model to calculate fire risk



