# Feature and Target Columns

This document summarizes the feature columns and target columns used in the FFKAN modeling workflow for hourly solar power prediction.

## Overview
- Source: FFKAN notebook configuration and training pipeline
- Scaling: Features are standardized via StandardScaler (zero mean, unit variance)
- Time granularity: Hourly data with cyclical encodings

## Target Columns
- Primary: PV(W) — measured solar power output in watts
- Alternatives:
  - Clearsky_Index — ratio of actual PV(W) to clear-sky expected power
  - PV(W)_error — residual between actual PV(W) and clear-sky expected power
  - PV(W)_error_index — residual index form relative to clear-sky expected power

## Feature Columns

| Column Name                         | Description                                                         | Type            | Notes |
|-------------------------------------|----------------------------------------------------------------------|-----------------|-------|
| Temperature(C)                      | Ambient air temperature                                              | numeric (float) | Physical sensor measurement |
| Humidity(%)                         | Relative humidity percentage                                         | numeric (float) | Physical sensor measurement |
| Sunshine Duration                   | Duration of sunshine over the hour                                  | numeric (float) | Units depend on source; proxy for irradiance |
| Precipitation(mm)                   | Hourly precipitation depth                                           | numeric (float) | Physical sensor measurement |
| Dew Point(C)                        | Dew point temperature                                                | numeric (float) | Derived from temperature/humidity |
| Wind Direction(deg)                 | Wind direction in degrees (0–360)                                    | numeric (float) | Cyclical variable; consider sine/cosine transforms |
| Wind Speed(m/s)                     | Wind speed                                                           | numeric (float) | Physical sensor measurement |
| Wind Gust(m/s)                      | Peak wind gust                                                       | numeric (float) | Physical sensor measurement |
| Pressure(hPa)                       | Atmospheric pressure                                                 | numeric (float) | Physical sensor measurement |
| Wind Cooling                        | Derived wind-cooling / wind-chill feature                            | numeric (float) | Engineered feature (temperature × wind) |
| Power_ClearSky_Pane_I(W)            | Clear-sky expected power for Pane I                                  | numeric (float) | Model-derived, depends on panel geometry |
| Power_ClearSky_Pane_II(W)           | Clear-sky expected power for Pane II                                 | numeric (float) | Model-derived, depends on panel geometry |
| Total_Power_ClearSky_Output(W)      | Total clear-sky expected power output                                | numeric (float) | Sum of pane-level clear-sky outputs |
| Month_Sin                           | Sine encoding of month                                               | numeric (float) | Cyclical encoding (period = 12 months) |
| Month_Cos                           | Cosine encoding of month                                             | numeric (float) | Cyclical encoding (period = 12 months) |
| DayOfYear_Sin                       | Sine encoding of day of year                                         | numeric (float) | Cyclical encoding (period ≈ 365 days) |
| DayOfYear_Cos                       | Cosine encoding of day of year                                       | numeric (float) | Cyclical encoding (period ≈ 365 days) |
| HourOfDay_Sin                       | Sine encoding of hour of day                                         | numeric (float) | Cyclical encoding (period = 24 hours) |
| HourOfDay_Cos                       | Cosine encoding of hour of day                                       | numeric (float) | Cyclical encoding (period = 24 hours) |
| level2_good_visibility              | Good visibility conditions indicator                                 | binary (0/1)    | One-hot encoded category |
| level2_moderate_visibility          | Moderate visibility conditions indicator                             | binary (0/1)    | One-hot encoded category |
| level2_poor_visibility              | Poor visibility conditions indicator                                 | binary (0/1)    | One-hot encoded category |
| level2_precipitation                | Precipitation conditions indicator                                   | binary (0/1)    | One-hot encoded category |
| level2_severe_weather               | Severe weather conditions indicator                                  | binary (0/1)    | One-hot encoded category |

## Notes
- Clear-sky features provide a physically-informed baseline; the model learns deviations due to weather.
- Cyclical encodings preserve periodicity and avoid artificial discontinuities (e.g., 23 → 0 hours).
- All features are scaled before training; interpretations should consider standardized units.
- Column availability may vary slightly depending on data preprocessing; adjust as needed based on dataset dtypes.
