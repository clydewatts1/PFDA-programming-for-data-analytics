# Big Project

## Overview

This project explores solar generation forecasting using meteorological data (Copernicus, Meteostat) and ESB Microgen readings. Multiple machine learning approaches are evaluated, including tree ensembles (Random Forest, AdaBoost, XGBoost), neural networks (PyTorch ANN), and Kolmogorov-Arnold Network (KAN) variants.  
  
Special attention is given to residual analysis (Bland-Altman, Q-Q plots) to identify systematic bias and heavy-tailed error distributions common in solar forecasting. KANs are employed as a novel methodology (introduced in 2024) to overcome the 'black box' limitations of standard ANNs. They explicitly demonstrate the additive nature of the features, offering interpretability comparable to Random Forest decision trees.  


## Project Requirements

For full project requirements and specifications, see [Project Description.pdf](documentation/Project%20Description.pdf).

## Objectives

- Build reproducible data pipelines for solar and weather datasets.
- Train and compare several regression models for generation forecasting.
- Evaluate models with standard metrics (RMSE, MAE, R²).
- Persist trained models and report test metrics for transparent comparison.


## Conclusion

This project establishes Random Forest as the baseline for forecasting solar PV output, achieving an acceptable degree of accuracy given the weather data. Alternative approaches, including Gradient Boosting (XGBoost, AdaBoost), Artificial Neural Networks (ANN), and Kolmogorov-Arnold Networks (KAN), yielded similar accuracy, with the simple ANN emerging as the best-performing model. All these models attempt to capture the complex, non-linear nature of solar and weather forecasting.

The KAN model offers a distinct advantage by not functioning as a 'black box'; instead, it reveals the underlying physical additive and subtractive nature of the feature dataset.

Despite the baseline's good accuracy, residual analysis (using Q-Q and Bland-Altman plots) reveals systematic bias, heavy-tailed error distributions, and evidence of overfitting across all models. This suggests that there is significant room for future improvements.



## Data Sources

- Copernicus Solar Radiation data
- ESB Microgen data
- Meteostat weather data/cache

Raw and processed files live under `data/`, with caches and derived artifacts organized for reproducibility.

## Methods

- Feature engineering from raw sources into model-ready datasets.
- Model training using ensemble methods and neural networks.
- Hyperparameter tuning and evaluation via held-out test sets.
- Results logged to CSVs in `results/` and models saved under `model/`.

## Directory Structure

```text
big_project/
├── big_project.ipynb
├── big_project_adaboost_hourly.ipynb
├── big_project_ANN.ipynb
├── big_project_FFKAN.ipynb
├── big_project_gpr_hourly.ipynb
├── big_project_KAN.ipynb
├── big_project_pygam_hourly.ipynb
├── big_project_random_forest_hourly.ipynb
├── big_project_svr_hourly.ipynb
├── big_project_xboost_hourly.ipynb
├── cheatsheet.md
├── cheatsheet_qq_plots.ipynb
├── cheatsheet_residual_plots.ipynb
├── cheatshet_bland_alterman_plot.ipynb
├── feature_columns.md
├── README.md
├── requirements.txt
├── solar_xboost.json
├── __pycache__/
├── data/
│   ├── db_sqlite/
│   │   └── big_project_db.sqlite3
│   ├── meteostat_cache/
│   │   └── stations/
│   ├── processed_data/
│   │   ├── Copernicus_Solar_Data_Bettystown_2024_2025.csv
│   │   ├── Copernicus_Solar_Data_Bettystown_Enriched_2024_2025.csv
│   │   ├── daily_esb_microgen_data.*
│   │   ├── daily_solar_data.*
│   │   ├── df_raw_daily_*.csv
│   │   ├── df_raw_monthly_solar.csv
│   │   ├── df_raw_yearly_solar.csv
│   │   ├── df_weather.csv
│   │   └── ...
│   ├── raw_data/
│   │   ├── copernicus/
│   │   ├── esb/
│   │   └── ...
│   └── training_data/
├── documentation/
│   └── Project Description.pdf
├── figures/
├── images/
│   └── ESB_SOLAR.drawio
├── model/
│   ├── 0.*_{cache_data,config.yml,state}
│   ├── history.txt
│   ├── kan_model_target.*
│   ├── pytorch_ann_model.pth
│   └── ...
├── results/
│   ├── adaboost_regressor_hourly_test_metrics.csv
│   ├── ann_test_metrics.csv
│   ├── ffkan_test_metrics.csv
│   ├── kan_test_metrics.csv
│   ├── random_forest_regressor_hourly_test_metrics.csv
│   └── xgboost_regressor_hourly_test_metrics.csv
└── sandbox/
    ├── big_project_adaboost.ipynb
    ├── big_project_tft_hourly.ipynb
    ├── big_project_validate_timezones.ipynb
    ├── big_project_xboost.ipynb
    ├── fftKAN.py
    ├── GPR_IMPLEMENTATION_NOTES.md
    ├── GPR_QUICK_START.md
    ├── meteostat .ipynb
    └── nasa.ipynb
```

## Setup

- Prerequisites: Python 3.10+ and Jupyter Lab/Notebook.
- Create/activate a virtual environment (recommended).
- Install dependencies:

```bash
pip install -r big_project/requirements.txt
```

## Usage

- End-to-end: open and run `big_project/big_project.ipynb`.
- Individual models: run the corresponding notebooks (e.g., `big_project/big_project_xboost_hourly.ipynb`).
- Data preparation: review `data/` contents and any preprocessing notebooks in `sandbox/` as needed.

## Results & Artifacts

- Trained models: saved under `big_project/model/`.
- Metrics: CSV summaries in `big_project/results/` (e.g., RMSE, MAE, R²).
- Figures: plots and diagrams under `big_project/figures/` and `big_project/images/`.

## Evaluation Metrics

- RMSE: root mean squared error for overall error magnitude.
- MAE: mean absolute error for average deviation.
- R²: coefficient of determination for explained variance.

## AI Usage

This project used AI tools to support learning and development:

- GitHub Copilot (VS Code): Brainstorming ideas, study aid for concepts, and code assistant for suggestions and automation.
- Google Gemini: Brainstorming approaches, study aid for research and explanation, and code assistant for drafting and refinement.

Notes:
- To Be Filled In: specific prompts, sessions, and concrete contributions (e.g., which notebooks or functions were assisted).
- Add dates/versions if required by coursework guidelines.

## Academic Integrity

This work is intended for coursework. Cite all data sources appropriately and ensure any external code or libraries are used within academic guidelines.

### References

- SolisCloud: https://www.soliscloud.com/
- Solis Station Details: https://www.soliscloud.com/station/stationDetails/generalSituation/1298491919449681542?glyun_vue2=%2F%23%2Fstation
- Meteostat: https://meteostat.net/en/
- Meteostat Formats: https://dev.meteostat.net/formats.html#time-format
- Dublin Airport Hourly Data: https://data.gov.ie/dataset/dublin-airport-hourly-data
- Dublin Airport Weather CSV: https://cli.fusio.net/cli/climate_data/webdata/hly532.csv
- Copernicus ADS Requests: https://ads.atmosphere.copernicus.eu/requests?tab=all
- CAMS Solar Radiation Timeseries: https://ads.atmosphere.copernicus.eu/datasets/cams-solar-radiation-timeseries?tab=overview
- PVLIB Documentation: https://pvlib-python.readthedocs.io/en/stable/
- SQLite FAQ (schema reference): https://sqlite.org/faq.html#:~:text=If%20you%20are%20running%20the,including%20all%20tables%20and%20indices.
- pandas `read_excel`: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
- pandas `DataFrame.to_csv`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
- pandas `DataFrame.to_sql`: https://pandas.pydata.org/pandas-docs/version/2.1.3/reference/api/pandas.DataFrame.to_sql.html
- Scikit-learn `RandomForestClassifier`: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- Scikit-learn `train_test_split`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- Random Forest (Wikipedia): https://en.wikipedia.org/wiki/Random_forest
- Random Forest (DataCamp tutorial): https://www.datacamp.com/tutorial/random-forests-classifier-python
- Random Forest (Shelf.io overview): https://shelf.io/blog/random-forests-in-machine-learning/
- Google Decision Forests overview: https://developers.google.com/machine-learning/decision-forests/random-forests
- RMSE explanation (Statistics by Jim): https://statisticsbyjim.com/regression/root-mean-square-error-rmse/
- RMSE in Google ML Crash Course: https://developers.google.com/machine-learning/crash-course/linear-regression/loss
- RMSE definition (Deepchecks): https://www.deepchecks.com/glossary/root-mean-square-error/#:~:text=RMSE%20%3D%20sqrt%20%5B(%CE%A3(Pi,Oi)%C2%B2)%20%2F%20n%5D&text=This%20calculation%20serves%20as%20a,the%20values%20observed%20in%20reality.
- Bland–Altman plot (Wikipedia): https://en.wikipedia.org/wiki/Bland%E2%80%93Altman_plot
- Seaborn `regplot`: https://seaborn.pydata.org/generated/seaborn.regplot.html
- Seaborn `histplot`: https://seaborn.pydata.org/generated/seaborn.histplot.html
- Seaborn `boxplot`: https://seaborn.pydata.org/generated/seaborn.boxplot.html
- Seaborn `violinplot`: https://seaborn.pydata.org/generated/seaborn.violinplot.html
- Solar forecasting with Random Forest (ScienceDirect): https://www.sciencedirect.com/science/article/abs/pii/S0960148116311648
- Solar forecasting with Random Forest (HAL): https://univ-corse.hal.science/hal-01426321v1/document
- Data split and leakage discussion (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC9505493/#:~:text=To%20determine%20the%20subset%2C%20we,dataset%20into%20balanced%20data%20subsets.
- Data leakage overview (IBM): https://www.ibm.com/think/topics/data-leakage-machine-learning#:~:text=Data%20leakage%20happens%20when%20data,production%2C%20it%20becomes%20entirely%20inaccurate.
- Kaggle discussion on splitting: https://www.kaggle.com/discussions/getting-started/551515
- Forecasting: Principles and Practice: http://103.203.175.90:81/fdScript/RootOfEBooks/E%20Book%20collection%20-%202025/MED/Forecasting_%20Principles%20and%20Practice.pdf
- Gemini prompt (example): https://gemini.google.com/share/54cd534a5aeb

## Contributors

- Clyde Watts

## Acknowledgements

- Copernicus, Meteostat, and ESB Microgen data providers.
- Open-source libraries enabling model training and evaluation.
 - Google Gemini: research assistance and idea exploration.
 - GitHub Copilot: code suggestions and automation within VS Code.

