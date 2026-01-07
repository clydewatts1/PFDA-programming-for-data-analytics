# Gaussian Process Regression (GPR) Implementation for Solar Prediction

## Overview
This document describes the implementation of Gaussian Process Regression (GPR) for solar power prediction based on weather data, following the structure of `big_project_svr_hourly.ipynb`.

## File Created
- **big_project_gpr_hourly.ipynb**: Complete notebook implementing GPR for hourly solar power prediction

## GPR Implementation Details

### 1. Model Architecture
The GPR model uses a composite kernel specifically designed for solar prediction:

```python
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ExpSineSquared, ConstantKernel as C

kernel = (
    C(1.0, (1e-3, 1e3)) * RBF(length_scale=10.0, length_scale_bounds=(1e-2, 1e3)) +
    C(1.0, (1e-3, 1e3)) * ExpSineSquared(length_scale=1.0, periodicity=24.0, 
                                          length_scale_bounds=(1e-2, 1e2),
                                          periodicity_bounds=(20.0, 28.0)) +
    WhiteKernel(noise_level=1.0, noise_level_bounds=(1e-5, 1e2))
)
```

#### Kernel Components:
1. **RBF (Radial Basis Function) Kernel**: 
   - Captures smooth, continuous variations in solar power
   - Length scale initialized at 10.0 for hourly data correlation
   - Bounds allow optimization between 0.01 and 1000

2. **ExpSineSquared (Periodic) Kernel**:
   - Specifically tuned for **daily solar patterns** (24-hour periodicity)
   - Periodicity bounds (20-28 hours) allow slight variation around 24 hours
   - Critical for capturing sunrise/sunset patterns and daytime peaks

3. **WhiteKernel**:
   - Models observation noise and measurement uncertainties
   - Essential for numerical stability in GP calculations

### 2. GPR-Specific Hyperparameters

```python
gpr_model = GaussianProcessRegressor(
    kernel=kernel,
    n_restarts_optimizer=10,  # Multiple random starts for better optimization
    alpha=1e-10,              # Numerical stability (Tikhonov regularization)
    normalize_y=True,         # Normalizes target values for better convergence
    random_state=42           # Reproducibility
)
```

#### Key Parameters for Solar Prediction:
- **n_restarts_optimizer=10**: Important because kernel hyperparameter optimization is non-convex. Multiple restarts help find better local optima.
- **normalize_y=True**: Solar power has wide ranges (0W to several kW), normalization helps GP convergence
- **alpha=1e-10**: Small noise term for numerical stability without over-smoothing

### 3. GPR-Specific Metrics

In addition to standard metrics (RMSE, MAE, R²), the implementation includes:

#### Log Marginal Likelihood
```python
log_marginal_likelihood = gpr_model.log_marginal_likelihood(gpr_model.kernel_.theta)
```
- **What it measures**: The probability of observing the training data given the model
- **Why it matters**: 
  - Higher values indicate better model fit
  - Used internally for kernel hyperparameter optimization
  - Helps detect overfitting (extremely high values) or underfitting (very low values)

#### Optimized Kernel Parameters
```python
print(f"Optimized kernel: {gpr_model.kernel_}")
```
- Shows how the kernel parameters were tuned during training
- Useful for understanding what patterns the model learned (e.g., actual periodicity discovered)

### 4. Solar-Specific Tuning Applied

#### a) Periodic Kernel for Daily Patterns
- Solar power has strong daily periodicity (day/night cycles)
- ExpSineSquared kernel with 24-hour base period captures this
- Periodicity bounds (20-28 hours) allow flexibility for seasonal variations

#### b) Feature Engineering (inherited from SVR notebook)
- Temporal features: `Month_Sin`, `DayOfYear_Sin`, `HourOfDay_Sin`
- Weather features: Temperature, Humidity, Sunshine Duration, etc.
- Clear sky output: `Total_Power_ClearSky_Output(W)` - theoretical maximum

#### c) Target Variable Options
The notebook supports multiple target formulations:
- `PV(W)`: Direct power output
- `Clearsky_Index`: Ratio of actual to clear-sky output
- `PV(W)_error`: Deviation from clear-sky prediction
- `PV(W)_error_index`: Indexed error term

### 5. Advantages of GPR for Solar Prediction

1. **Uncertainty Quantification**: GPR has the capability to provide prediction intervals with confidence bounds. This feature is not utilized in the current implementation but can be easily added by using the `return_std=True` parameter in the `predict()` method.
2. **Non-parametric**: Automatically adapts to data complexity
3. **Kernel Flexibility**: Can combine multiple patterns (smooth trends + periodicity)
4. **Small Data Performance**: Often outperforms other methods with limited training data

### 6. Computational Considerations

**Scalability**: GPR has O(n³) computational complexity for training
- Current implementation suitable for datasets up to ~10,000 samples
- For larger datasets, consider:
  - Sparse GPs
  - Inducing points
  - Approximate inference methods

### 7. Output Files

Results are saved to:
```
results/gpr_regressor_hourly_test_metrics.csv
```

Additional fields compared to SVR version:
- Log Marginal Likelihood
- Optimized Kernel parameters
- Explained Variance (for both target and PV(W))

## Comparison with SVR

| Aspect | SVR | GPR |
|--------|-----|-----|
| Kernel | RBF only | RBF + Periodic + White Noise |
| Periodicity | Not captured | Explicit 24-hour periodicity |
| Uncertainty | No | Yes (available) |
| Scalability | Better (O(n²)) | Limited (O(n³)) |
| Metrics | Standard only | + Log Marginal Likelihood |
| Hyperparameters | Manual tuning | Automatic kernel optimization |

## Usage

1. Ensure training data exists in: `big_project/data/training_data/`
2. Open `big_project_gpr_hourly.ipynb` in Jupyter
3. Run cells sequentially
4. Results will be saved to `results/gpr_regressor_hourly_test_metrics.csv`

## Future Enhancements

1. **Prediction Intervals**: Add uncertainty quantification
2. **Sparse GP**: For larger datasets
3. **Multi-output GP**: Predict multiple targets simultaneously
4. **Custom Kernels**: Add seasonal (yearly) periodicity for long-term patterns
5. **Hyperparameter Grid Search**: Systematic kernel parameter optimization

## References

- Scikit-learn GaussianProcessRegressor: https://scikit-learn.org/stable/modules/gaussian_process.html
- Rasmussen & Williams (2006): "Gaussian Processes for Machine Learning"
- Solar forecasting with GPs: Relevant domain literature on periodic kernel applications
