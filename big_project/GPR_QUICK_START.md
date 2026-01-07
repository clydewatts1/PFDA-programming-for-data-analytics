# GPR Quick Start Guide

## What Was Implemented

Based on your request to implement GPR following the structure of `big_project_svr_hourly.ipynb`, I have created a complete Gaussian Process Regression implementation for solar power prediction.

## Files Created

1. **big_project_gpr_hourly.ipynb** - Main notebook implementing GPR
2. **GPR_IMPLEMENTATION_NOTES.md** - Detailed technical documentation
3. **GPR_QUICK_START.md** - This quick start guide

## Key Features

### 1. Solar-Optimized Kernel
The GPR model uses a composite kernel specifically designed for solar prediction:
- **RBF kernel**: Captures smooth variations in power output
- **ExpSineSquared kernel**: Models 24-hour daily periodicity (sunrise/sunset patterns)
- **WhiteKernel**: Handles observation noise

### 2. GPR-Specific Metrics
In addition to standard metrics (RMSE, MAE, R²), the implementation includes:
- **Log Marginal Likelihood**: Measures model quality and prevents overfitting
- **Optimized Kernel Parameters**: Shows learned patterns (e.g., discovered periodicity)
- **Explained Variance**: Additional accuracy measure

### 3. Solar Prediction Tuning
- Periodic kernel with 24-hour base period for daily patterns
- Flexible periodicity bounds (20-28 hours) for seasonal variations
- Multiple optimization restarts (n_restarts_optimizer=10) for better convergence
- Target normalization for improved stability

## How to Use

1. **Open the notebook**:
   ```bash
   jupyter notebook big_project/big_project_gpr_hourly.ipynb
   ```

2. **Run cells sequentially**:
   - Cell 0-2: Setup and imports
   - Cell 7: Load training/testing data
   - Cell 11-12: Configure features and target
   - Cell 13: Train GPR model (this may take a few minutes)
   - Cell 16: View metrics including GPR-specific measures
   - Cell 18-23: Visualization plots
   - Cell 26: Save results to CSV

3. **Results location**:
   ```
   results/gpr_regressor_hourly_test_metrics.csv
   ```

## Target Variable Options

The notebook supports multiple target formulations (configured in Cell 11):
- `PV(W)`: Direct power output prediction
- `Clearsky_Index`: Ratio of actual to theoretical clear-sky output
- `PV(W)_error`: Deviation from clear-sky baseline (default)
- `PV(W)_error_index`: Indexed error formulation

## Expected Performance

GPR typically provides:
- **Better uncertainty quantification** than SVR (can be enabled)
- **Automatic pattern discovery** through kernel optimization
- **Good performance with limited data** due to Bayesian approach
- **Slower training** than SVR (O(n³) vs O(n²) complexity)

## Customization Options

### Change kernel parameters (Cell 13):
```python
# Adjust length scales for different smoothness
RBF(length_scale=10.0, length_scale_bounds=(1e-2, 1e3))

# Adjust periodicity for different patterns
ExpSineSquared(length_scale=1.0, periodicity=24.0, 
               periodicity_bounds=(20.0, 28.0))

# Adjust noise modeling
WhiteKernel(noise_level=1.0, noise_level_bounds=(1e-5, 1e2))
```

### Enable uncertainty quantification:
In Cell 13, change prediction to:
```python
y_test_pred, y_test_std = gpr_model.predict(X_test, return_std=True)
```
This provides confidence intervals for each prediction.

## Comparison with SVR

| Feature | SVR | GPR |
|---------|-----|-----|
| Periodicity modeling | No | Yes (24h explicit) |
| Uncertainty | No | Yes (available) |
| Training time | Faster | Slower |
| Kernel flexibility | Limited | High |
| Hyperparameter tuning | Manual | Automatic |
| Best for | Large datasets | Small-medium datasets |

## Troubleshooting

### If training is too slow:
- Reduce training data size in Cell 7
- Reduce `n_restarts_optimizer` from 10 to 5 in Cell 13
- Consider using sparse GP methods (see GPR_IMPLEMENTATION_NOTES.md)

### If results are poor:
- Check kernel parameter bounds are reasonable
- Verify feature scaling/normalization
- Try different target variables (Cell 11)
- Increase `n_restarts_optimizer` for better optimization

### If memory errors occur:
- GPR requires O(n²) memory for kernel matrix
- Reduce training data size
- Use batch prediction for test set

## Next Steps

1. **Run the notebook** and compare results with SVR
2. **Tune hyperparameters** based on Log Marginal Likelihood
3. **Add uncertainty quantification** for prediction intervals
4. **Experiment with different kernels** for seasonal patterns
5. **Compare multiple target formulations** to find best approach

## Support

For detailed technical information, see:
- **GPR_IMPLEMENTATION_NOTES.md** - Comprehensive implementation guide
- **big_project_svr_hourly.ipynb** - Original SVR implementation for comparison

For questions about kernel design or solar-specific tuning, refer to the kernel comments in Cell 13 of the notebook.
