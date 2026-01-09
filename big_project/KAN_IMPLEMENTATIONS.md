# KAN Implementation Comparison

This document compares the two Kolmogorov-Arnold Network (KAN) implementations used in this project.

## Overview

Two different KAN libraries are used:
1. **PyKAN** (`big_project_KAN.ipynb`) - Original implementation
2. **Efficient KAN** (`big_project_efficient_KAN.ipynb`) - Optimized implementation

## Key Differences

### 1. Library Source

| Feature | PyKAN | Efficient KAN |
|---------|-------|---------------|
| Repository | https://github.com/KindXiaoming/pykan | https://github.com/Blealtan/efficient-kan |
| Installation | `pip install pykan` | `pip install git+https://github.com/Blealtan/efficient-kan.git` |
| Status | Available on PyPI | GitHub only |

### 2. API and Training

| Feature | PyKAN | Efficient KAN |
|---------|-------|---------------|
| Training Method | Custom `model.fit()` method | Standard PyTorch training loop |
| Optimizer | Built-in (Adam, LBFGS) | Manual setup (Adam, AdamW, etc.) |
| Pruning | Built-in `model.prune()` | Not available |
| Grid Update | Automatic during training | Manual via `update_grid()` if needed |

### 3. Model Architecture

| Feature | PyKAN | Efficient KAN |
|---------|-------|---------------|
| Model Creation | `kan.KAN(width=[...], grid=..., k=...)` | `KAN(layers_hidden=[...], grid_size=..., spline_order=...)` |
| Parameter Names | `width`, `grid`, `k` | `layers_hidden`, `grid_size`, `spline_order` |
| Additional Options | More symbolic/interpretability features | Focus on performance and efficiency |

### 4. Memory Efficiency

**PyKAN:**
- Expands intermediate variables to shape `(batch_size, out_features, in_features)`
- More memory intensive
- Supports symbolic representation and interpretability features

**Efficient KAN:**
- Reformulated computation as matrix multiplication
- Significantly reduced memory footprint
- Faster training and inference
- L1 regularization on weights instead of samples

### 5. Model Saving

| Feature | PyKAN | Efficient KAN |
|---------|-------|---------------|
| Save Method | `model.saveckpt()` | `torch.save()` (standard PyTorch) |
| File Format | `.ckpt` (custom) | `.pth` (PyTorch state dict) |
| Load Method | `kan.KAN.loadckpt()` | `model.load_state_dict()` |

### 6. Feature Availability

| Feature | PyKAN | Efficient KAN |
|---------|-------|---------------|
| Symbolic Formula | ✓ `auto_symbolic()` | ✗ Not available |
| Built-in Plotting | ✓ `model.plot()` | ✗ Not available |
| Pruning | ✓ `model.prune()` | ✗ Not available |
| Custom Visualizations | ✓ Via helper functions | ✓ Via helper functions |
| Training History | ✓ Returned by `fit()` | ✓ Manual tracking |

## Code Examples

### PyKAN (Original)

```python
import kan

# Create model
model = kan.KAN(width=[input_dim, 7, 1], grid=12, k=3, seed=42)

# Train with custom fit method
results = model.fit(dataset, opt='Adam', steps=100, lamb=0.001)

# Prune unnecessary connections
model = model.prune()

# Refine the model
results = model.fit(dataset, opt='LBFGS', steps=10)

# Save model
model.saveckpt("model.ckpt")
```

### Efficient KAN (Optimized)

```python
from efficient_kan import KAN
import torch.optim as optim

# Create model
model = KAN(
    layers_hidden=[input_dim, 7, 1],
    grid_size=12,
    spline_order=3
).to(device)

# Setup optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = torch.nn.MSELoss()

# Training loop
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    predictions = model(train_input)
    loss = criterion(predictions, train_label)
    reg_loss = model.regularization_loss()
    total_loss = loss + 0.001 * reg_loss
    total_loss.backward()
    optimizer.step()

# Save model
torch.save({
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict()
}, "model.pth")
```

## When to Use Which?

### Use PyKAN when:
- You need symbolic formula extraction
- Interpretability is critical
- You want built-in pruning and automatic optimization
- Memory is not a constraint
- You prefer high-level API with less boilerplate

### Use Efficient KAN when:
- Memory efficiency is important
- You have large datasets
- You need faster training/inference
- You prefer standard PyTorch workflow
- You want more control over training process
- You're familiar with PyTorch training loops

## Performance Considerations

**Memory Usage:**
- Efficient KAN uses significantly less memory (can handle larger batch sizes)
- PyKAN may require smaller batch sizes for the same hardware

**Training Speed:**
- Efficient KAN is generally faster per epoch
- PyKAN has more overhead due to expanded tensors

**Accuracy:**
- Both implementations should achieve similar accuracy
- Results may vary slightly due to different regularization approaches

## Conclusion

Both implementations are valid approaches to KAN models. **PyKAN** offers more interpretability features and a simpler API, while **Efficient KAN** provides better performance and follows standard PyTorch conventions. The choice depends on your specific requirements and constraints.

For this solar forecasting project, both implementations can achieve good results, but Efficient KAN may be preferred for:
- Larger datasets (more hourly data points)
- Limited computational resources
- Integration with existing PyTorch pipelines
- Need for custom training loops or schedulers
