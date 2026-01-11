# Temporal Kolmogorov-Arnold Networks (TKAN) Implementation

## Overview

This directory contains a **Temporal KAN (TKAN)** implementation using **PyTorch** for solar power prediction. The implementation is based on the `big_project_efficient_KAN.ipynb` notebook but with explicit temporal encoding from the DateTime column.

## Files

- **`tkan_implementation.py`**: Core TKAN implementation
  - `TemporalEncoding`: Sinusoidal temporal encoding layer
  - `TKANLayer`: Single TKAN layer with learnable activations
  - `TKAN`: Complete TKAN network
  - `extract_temporal_features()`: Helper to extract temporal features from DataFrame

- **`big_project_TKAN.ipynb`**: Complete training notebook
  - Data loading and preprocessing
  - Temporal feature extraction
  - Model training and evaluation
  - Visualization and analysis

## Key Differences from Efficient KAN

| Feature | Efficient KAN | TKAN (This Implementation) |
|---------|---------------|----------------------------|
| Framework | PyTorch | PyTorch ✓ |
| Temporal Features | Implicit (through other features) | **Explicit from DateTime column** ✓ |
| Temporal Encoding | None | **Sinusoidal embeddings** ✓ |
| DateTime Usage | Not directly used | **hour, day_of_week, day_of_year, month** ✓ |
| Activation Functions | B-splines (efficient-kan library) | **RBF kernels** (custom) |

## Architecture

### Temporal Encoding

The key innovation is the **Temporal Encoding** layer that converts discrete time features into continuous sinusoidal embeddings:

```python
# Extract from DateTime column
hour (0-23) → sin/cos encoding
day_of_week (0-6) → sin/cos encoding
day_of_year (0-365) → sin/cos encoding
month (1-12) → sin/cos encoding
```

This creates a 16-dimensional temporal embedding that captures:
- **Daily patterns** (hour)
- **Weekly patterns** (day_of_week)
- **Seasonal patterns** (day_of_year, month)

### Network Architecture

```
Input Features (weather/solar) 
    ↓
+ Temporal Encoding (16 dims)
    ↓
TKAN Layer 1 (input_dim+16 → hidden_dim)
    ↓
TKAN Layer 2 (hidden_dim → output_dim)
    ↓
Output (power prediction)
```

Default configuration:
- Input: 10 weather/solar features
- Temporal: 16 dimensions
- Hidden: 32 neurons
- Output: 1 (power prediction)
- Grid size: 10 points for learnable functions

## Usage

### Basic Example

```python
from tkan_implementation import TKAN, extract_temporal_features
import pandas as pd
import torch

# Load data with DateTime column
df = pd.read_feather('data.feather')

# Extract temporal features
temporal_features = extract_temporal_features(df, datetime_col='DateTime')

# Create model
model = TKAN(
    layers_hidden=[10, 32, 1],
    grid_size=10,
    use_temporal=True,
    temporal_dim=16
)

# Forward pass
x = torch.randn(batch_size, 10)  # Weather/solar features
output = model(x, temporal_features)
```

### Training

See `big_project_TKAN.ipynb` for complete training pipeline:

1. Load hourly solar data
2. Extract temporal features from DateTime
3. Scale features
4. Create TKAN model
5. Train with MSE + L1 regularization
6. Evaluate with RMSE, MAE, R²

## Mathematical Background

### Sinusoidal Temporal Encoding

For each temporal feature $t$ (normalized to $[0, 2\pi]$):

$$
\text{TE}(t, 2i) = \sin(2^i \cdot t)
$$

$$
\text{TE}(t, 2i+1) = \cos(2^i \cdot t)
$$

This creates embeddings that:
- Are **periodic** (suitable for cyclic time patterns)
- Have different **frequencies** (capturing multi-scale patterns)
- Are **smooth** and **differentiable**

### TKAN Layer

Each TKAN layer computes:

$$
y = W_{base} \cdot [x, \text{TE}(t)] + \sum_{i,g} w_{i,g} \cdot \phi(x_i, grid_g)
$$

Where:
- $x$: Input features
- $\text{TE}(t)$: Temporal encoding
- $W_{base}$: Base linear weights
- $w_{i,g}$: Learnable weights for each input-grid pair
- $\phi$: RBF kernel function

## Requirements

```bash
pip install torch numpy pandas scikit-learn matplotlib seaborn
```

## Performance

Expected performance on hourly solar data:
- **RMSE**: Similar to Efficient KAN (~150-200 W)
- **MAE**: Similar to Efficient KAN (~100-150 W)
- **R²**: 0.85-0.95 depending on data and hyperparameters

The temporal encoding should provide:
- Better generalization to different times of day
- Improved handling of seasonal patterns
- More interpretable time-dependent behavior

## Hyperparameter Tuning

Key parameters to adjust:

1. **`temporal_dim`** (default: 16)
   - Dimension of temporal encoding
   - Try: 8, 16, 32

2. **`grid_size`** (default: 10)
   - Number of grid points for learnable functions
   - Try: 5, 10, 20

3. **`hidden_dim`** (default: 32)
   - Number of hidden neurons
   - Try: 16, 32, 64

4. **`reg_lambda`** (default: 0.001)
   - L1 regularization strength
   - Try: 0.0001, 0.001, 0.01

## Comparison with Other Approaches

| Model | Framework | Temporal Handling | Complexity |
|-------|-----------|-------------------|------------|
| Efficient KAN | PyTorch | Implicit | Medium |
| TKAN | PyTorch | Explicit (sinusoidal) | Medium |
| Transformers | PyTorch | Positional encoding | High |
| LSTMs | PyTorch | Sequential | High |
| Standard ANN | PyTorch | None | Low |

## Future Improvements

1. **Attention mechanism** for temporal features
2. **Learnable temporal embedding** (not just sinusoidal)
3. **Multi-scale temporal aggregation**
4. **Hybrid TKAN-LSTM** architecture
5. **Meta-learning** for different seasons

## References

- **Kolmogorov-Arnold Networks**: [arXiv:2404.19756](https://arxiv.org/abs/2404.19756)
- **Attention Is All You Need** (Positional Encoding): [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- **Efficient-KAN**: [GitHub](https://github.com/Blealtan/efficient-kan)

## Author

**Clyde Watts**  
PFDA Programming for Data Analytics  
Date: 2025-01-11

## License

This implementation is part of the PFDA coursework.
