# Feature and Target Columns

Source of truth: random-forest feature configuration in [big_project.ipynb](../big_project.ipynb) (test_no "03" block). All columns listed below are defined in that block, including optional/commented features.

## Roles
- <span style="color:blue;">source</span>: input features provided to the model (may be optional/off by default)
- <span style="color:red;">target</span>: primary supervised learning target
- <span style="color:red;">target_equivalent</span>: alternate targets derived from the primary target

## Column Catalog

| Column Name                              | Description                                                    | Type             | Role                                 | Notes |
|------------------------------------------|----------------------------------------------------------------|------------------|--------------------------------------|-------|
| PV(W)                                    | Measured solar power output                                    | numeric (float)  | <span style="color:red;">target</span>            | Primary target; watt-level output |
| Clearsky_Index                           | PV(W) divided by clear-sky expected output                     | numeric (float)  | <span style="color:red;">target_equivalent</span> | Toggleable target in notebook |
| PV(W)_error                              | Residual between PV(W) and clear-sky expected output           | numeric (float)  | <span style="color:red;">target_equivalent</span> | Default target in RF block |
| PV(W)_error_index                        | Residual index relative to clear-sky expected output           | numeric (float)  | <span style="color:red;">target_equivalent</span> | Toggleable target in notebook |
| index                                    | Original row index                                             | integer          | <span style="color:blue;">source</span>            | Useful for debugging only |
| DateTime                                 | Timestamp for the hourly record                                | datetime         | <span style="color:blue;">source</span>            | Combines Date and Time |
| Date                                     | Calendar date                                                  | date             | <span style="color:blue;">source</span>            | Available in raw frame |
| Time                                     | Time of day                                                    | time             | <span style="color:blue;">source</span>            | Available in raw frame |
| Temperature(C)                           | Ambient temperature                                            | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Humidity(%)                              | Relative humidity                                              | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Sunshine Duration                        | Sunshine duration within the hour                              | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Condition Code                           | Meteostat condition code                                       | categorical      | <span style="color:blue;">source</span>            | Optional; commented out |
| Precipitation(mm)                        | Hourly precipitation depth                                     | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Dew Point(C)                             | Dew point temperature                                          | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Wind Direction(deg)                      | Wind direction                                                 | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Wind Speed(m/s)                          | Wind speed                                                     | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Wind Gust(m/s)                           | Wind gust                                                      | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Pressure(hPa)                            | Atmospheric pressure                                           | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Snow Depth(cm)                           | Snow depth                                                     | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Wind Cooling                             | Engineered wind-cooling metric                                 | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Temp_Momentum                            | Temperature momentum                                           | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Humidity_Momentum                        | Humidity momentum                                              | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| WindSpeed_Momentum                       | Wind speed momentum                                            | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Total_Power_ClearSky_Output(W)_Momentum  | Clear-sky power momentum                                       | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Temp_Lag1                                | Temperature lag                                                | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Humidity_Lag1                            | Humidity lag                                                   | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| WindSpeed_Lag1                           | Wind speed lag                                                 | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Total_Power_ClearSky_Output(W)_Lag1      | Clear-sky power lag                                            | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_clear                             | One-hot: clear weather                                         | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_cloudy                            | One-hot: cloudy weather                                        | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_fair                              | One-hot: fair weather                                          | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_fog                               | One-hot: fog                                                   | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_freezing_rain                     | One-hot: freezing rain                                         | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_heavy_rain                        | One-hot: heavy rain                                            | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_heavy_rain_shower                 | One-hot: heavy rain shower                                     | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_heavy_sleet                       | One-hot: heavy sleet                                           | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_light_rain                        | One-hot: light rain                                            | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_overcast                          | One-hot: overcast                                              | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_rain                              | One-hot: rain                                                  | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_rain_shower                       | One-hot: rain shower                                           | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_sleet                             | One-hot: sleet                                                 | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_sleet_shower                      | One-hot: sleet shower                                          | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level1_thunderstorm                      | One-hot: thunderstorm                                          | binary (0/1)     | <span style="color:blue;">source</span>            | Optional; commented out |
| level2_good_visibility                   | One-hot: good visibility                                       | binary (0/1)     | <span style="color:blue;">source</span>            | Auto-detected and appended |
| level2_moderate_visibility               | One-hot: moderate visibility                                   | binary (0/1)     | <span style="color:blue;">source</span>            | Auto-detected and appended |
| level2_poor_visibility                   | One-hot: poor visibility                                       | binary (0/1)     | <span style="color:blue;">source</span>            | Auto-detected and appended |
| level2_precipitation                     | One-hot: precipitation flag                                    | binary (0/1)     | <span style="color:blue;">source</span>            | Auto-detected and appended |
| level2_severe_weather                    | One-hot: severe weather flag                                   | binary (0/1)     | <span style="color:blue;">source</span>            | Auto-detected and appended |
| # Observation period                     | Observation period metadata                                    | numeric/string   | <span style="color:blue;">source</span>            | Optional; commented out |
| TOA                                       | Top-of-atmosphere irradiance                                   | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Clear sky GHI                            | Modeled clear-sky global horizontal irradiance                 | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Clear sky BHI                            | Modeled clear-sky beam horizontal irradiance                   | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Clear sky DHI                            | Modeled clear-sky diffuse horizontal irradiance                | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Clear sky BNI                            | Modeled clear-sky beam normal irradiance                       | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| GHI                                      | Global horizontal irradiance                                   | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| BHI                                      | Beam horizontal irradiance                                     | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| DHI                                      | Diffuse horizontal irradiance                                  | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| BNI                                      | Beam normal irradiance                                         | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Reliability,                             | Station reliability metric (string in source)                  | string           | <span style="color:blue;">source</span>            | Optional; commented out |
| POA_Pane_I(W/m^2)                        | Plane-of-array irradiance, pane I                              | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| POA_Pane_II(W/m^2)                       | Plane-of-array irradiance, pane II                             | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| POAC_Pane_I(W/m^2)                       | Clear-sky POA irradiance, pane I                               | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| POAC_Pane_II(W/m^2)                      | Clear-sky POA irradiance, pane II                              | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Power_Pane_I(W)                          | Observed pane I power                                          | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Power_Pane_II(W)                         | Observed pane II power                                         | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Power_ClearSky_Pane_I(W)                 | Clear-sky expected power, pane I                               | numeric (float)  | <span style="color:blue;">source</span>            | Included in base feature list |
| Power_ClearSky_Pane_II(W)                | Clear-sky expected power, pane II                              | numeric (float)  | <span style="color:blue;">source</span>            | Included in base feature list |
| Total_Power_Output(W)                    | Total observed power output                                    | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| Total_Power_ClearSky_Output(W)           | Total clear-sky expected power output                          | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| WeekOfYear                               | Week number                                                    | integer          | <span style="color:blue;">source</span>            | Optional; commented out |
| Month_Sin                                | Sine transform of month                                        | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| Month_Cos                                | Cosine transform of month                                      | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| DayOfYear_Sin                            | Sine transform of day-of-year                                  | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| DayOfYear_Cos                            | Cosine transform of day-of-year                                | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |
| HourOfDay_Sin                            | Sine transform of hour-of-day                                  | numeric (float)  | <span style="color:blue;">source</span>            | Included in active feature set |
| HourOfDay_Cos                            | Cosine transform of hour-of-day                                | numeric (float)  | <span style="color:blue;">source</span>            | Optional; commented out |

## Notes
- Active feature set (currently used): Temperature(C), Humidity(%), Sunshine Duration, Precipitation(mm), Dew Point(C), Wind Direction(deg), Wind Speed(m/s), Pressure(hPa), Wind Cooling, Total_Power_ClearSky_Output(W), Month_Sin, DayOfYear_Sin, HourOfDay_Sin, level2_*.
- All other source columns are defined in the notebook for experimentation even if commented out.
- Features are standardized before modeling; cyclical encodings preserve periodicity.
