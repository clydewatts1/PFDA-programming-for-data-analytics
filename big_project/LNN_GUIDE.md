# Liquid Neural Network (LNN) Implementation Guide

## Overview

This guide explains how to use the Liquid Neural Network (CfC - Closed-form Continuous-time) implementation for solar power prediction. The implementation is located in `big_project_LNN.ipynb`.

## What is a Liquid Neural Network?

Liquid Neural Networks (LNNs) are a type of recurrent neural network that uses continuous-time models inspired by biological neurons. The CfC (Closed-form Continuous-time) variant provides:

- **Better temporal modeling**: Unlike standard RNNs/LSTMs, CfC neurons model continuous-time dynamics
- **Improved long-term dependencies**: Better at capturing patterns over extended time sequences
- **Interpretability**: The continuous-time formulation is more interpretable than discrete-time RNNs
- **Efficiency**: Closed-form solution allows for faster computation than numerical ODE solvers

## Requirements

The implementation requires the following packages (already added to `requirements.txt`):

```bash
pip install torch>=2.0.0 ncps>=0.0.9 numpy pandas scikit-learn matplotlib seaborn pyarrow
```

## Architecture

The model architecture is:

```
Input (Weather Features, 24-hour sequences) 
  ↓
CfC Layer (AutoNCP wiring with 64 hidden units)
  ↓
Output (PV(W)_error prediction)
```

### Key Components:

1. **Input**: 3D tensor of shape `(batch_size, sequence_length=24, num_features)`
2. **CfC Layer**: Liquid neural network layer with AutoNCP wiring for sparse connectivity
3. **Output**: Single value representing the error/residual

## Data Flow

### 1. Data Preparation

The implementation uses a sliding window approach to create sequences:

```python
# Load training data
df_train = pd.read_feather("data/training_data/hourly_solar_training_data.feather")

# Features include:
# - Weather: Temperature, Humidity, Wind Speed, etc.
# - Time encodings: Month_Sin/Cos, DayOfYear_Sin/Cos, HourOfDay_Sin/Cos
# - Lag features: Previous hour and 24-hour lag values
# - Clear sky output: Total_Power_ClearSky_Output(W)

# Target:
# - PV(W)_error: Residual between actual and clear sky output
```

### 2. Sequence Creation

Tabular data is converted to 3D sequences using a sliding window:

```python
def create_sequences(data, target, sequence_length=24):
    """
    Creates overlapping sequences from tabular data.
    
    Input: (num_samples, num_features)
    Output: (num_samples - sequence_length + 1, sequence_length, num_features)
    """
    # Implementation creates sequences where each sample contains
    # the last 24 hours of weather data
```

### 3. Model Training

Standard PyTorch training loop with:
- **Loss**: MSE (Mean Squared Error)
- **Optimizer**: Adam (lr=0.001)
- **Batch size**: 64
- **Epochs**: 100 (configurable)

### 4. Prediction & Reconstruction

```python
# 1. Predict PV(W)_error (residual)
y_pred_error = model(X_test)

# 2. Reconstruct final PV(W) by adding back clear sky output
y_pred_pvw = y_pred_error + Total_Power_ClearSky_Output(W)

# 3. Clip negative values (solar power cannot be negative)
y_pred_pvw = np.clip(y_pred_pvw, 0, None)
```

## Usage

### Running the Notebook

1. Open `big_project_LNN.ipynb` in Jupyter:
   ```bash
   jupyter notebook big_project_LNN.ipynb
   ```

2. Run all cells sequentially

3. The notebook will:
   - Load training and testing data
   - Create sequences
   - Train the model
   - Make predictions
   - Calculate metrics
   - Generate visualizations

### Key Hyperparameters

You can modify these in the notebook:

```python
SEQUENCE_LENGTH = 24      # Hours of history to use
hidden_size = 64          # Number of hidden units in CfC layer
num_epochs = 100          # Training epochs
batch_size = 64           # Batch size for training
learning_rate = 0.001     # Adam optimizer learning rate
```

### Model Saving & Loading

The trained model is saved automatically:

```python
# Save
torch.save({
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'scaler': scaler,
    'sequence_length': SEQUENCE_LENGTH,
    'input_size': input_size,
    'hidden_size': hidden_size,
    'feature_cols': feature_cols
}, "model/liquid_neural_network_model.pth")

# Load
checkpoint = torch.load("model/liquid_neural_network_model.pth")
model.load_state_dict(checkpoint['model_state_dict'])
```

## Performance Metrics

The notebook calculates and displays:

1. **RMSE** (Root Mean Squared Error): Lower is better
2. **MAE** (Mean Absolute Error): Lower is better
3. **R²** (R-squared): Higher is better (0-1 range, 1 = perfect)
4. **Normalized RMSE & MAE**: Percentage-based metrics
5. **Accuracy**: Percentage accuracy score

Metrics are calculated for both:
- Direct predictions (PV(W)_error)
- Reconstructed PV(W) values

## Visualizations

The notebook generates:

1. **Training History**: Loss curves for training and validation
2. **Actual vs Predicted**: Scatter plot showing prediction accuracy
3. **Residual Plot**: Distribution of prediction errors
4. **Time Series Comparison**: Side-by-side comparison of actual vs predicted values

## Comparison with Random Forest

| Aspect | Random Forest | Liquid Neural Network |
|--------|---------------|----------------------|
| Input | Tabular (2D) | Sequential (3D) |
| Temporal Modeling | Via lag features only | Native temporal modeling |
| Training Time | Fast | Moderate |
| Interpretability | Feature importance | Continuous dynamics |
| Memory | Low | Moderate |
| Best For | Static patterns | Time-dependent patterns |

## Tips for Best Performance

1. **Sequence Length**: 24 hours works well for daily patterns; try 48-72 for longer dependencies
2. **Hidden Size**: Start with 64, increase if underfitting, decrease if overfitting
3. **Learning Rate**: 0.001 is a good default; reduce if training is unstable
4. **Epochs**: Monitor validation loss; stop when it plateaus or increases
5. **Features**: Include lag features (1h, 24h) for better temporal context

## Troubleshooting

### Low R² Score
- Increase training epochs
- Increase hidden size
- Add more lag features
- Check for data quality issues

### Model Overfitting
- Reduce hidden size
- Add dropout (modify model definition)
- Use early stopping
- Increase training data

### Memory Issues
- Reduce batch size
- Reduce sequence length
- Reduce hidden size
- Use smaller subsets for testing

## References

- **ncps Library**: [https://github.com/mlech26l/ncps](https://github.com/mlech26l/ncps)
- **Paper**: "Closed-form Continuous-time Models" - Lechner & Hasani et al.
- **PyTorch Documentation**: [https://pytorch.org/docs/](https://pytorch.org/docs/)

## Support

For issues or questions:
1. Check the notebook comments and markdown cells
2. Review this guide
3. Consult the ncps library documentation
4. Open an issue in the repository
