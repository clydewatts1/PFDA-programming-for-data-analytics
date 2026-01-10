# Quick Start Guide: Efficient KAN Notebook

This guide helps you get started with the `big_project_efficient_KAN.ipynb` notebook.

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Virtual environment (recommended)

## Installation Steps

### 1. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Base Requirements

```bash
# Navigate to project directory
cd big_project

# Install standard dependencies
pip install -r requirements.txt
```

### 3. Install Efficient KAN

The efficient-kan library is not available on PyPI and must be installed from GitHub:

```bash
pip install git+https://github.com/Blealtan/efficient-kan.git
```

**Note:** This will install the library directly from the GitHub repository.

### 4. Verify Installation

```python
# Test in Python
python -c "from efficient_kan import KAN; print('Efficient KAN installed successfully!')"
```

If you see the success message, you're ready to go!

## Running the Notebook

### Option 1: Jupyter Lab

```bash
jupyter lab big_project_efficient_KAN.ipynb
```

### Option 2: Jupyter Notebook

```bash
jupyter notebook big_project_efficient_KAN.ipynb
```

### Option 3: VS Code

1. Open the notebook file in VS Code
2. Select the Python kernel from your virtual environment
3. Run cells interactively

## Data Requirements

Make sure you have the required data files:

- `data/training_data/hourly_solar_full_data.feather`

If the data file is missing, you may need to run the main data preparation notebook first.

## Expected Runtime

- **Model Training**: ~5-10 minutes (100 epochs)
- **Full Notebook**: ~15-20 minutes

Times may vary based on hardware (GPU will be faster).

## GPU Support

The notebook will automatically use CUDA if available:

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
```

To check if GPU is being used:
```python
print(f"Using device: {device}")
```

## Common Issues

### Issue: ModuleNotFoundError: No module named 'efficient_kan'

**Solution:** Install from GitHub:
```bash
pip install git+https://github.com/Blealtan/efficient-kan.git
```

### Issue: CUDA out of memory

**Solution:** Reduce batch size or use CPU:
```python
device = torch.device('cpu')
```

### Issue: Data file not found

**Solution:** Run the main data preparation pipeline or check the data path in the notebook.

## Differences from PyKAN Version

If you're familiar with `big_project_KAN.ipynb`, here are the main differences:

1. **No custom fit() method** - Uses standard PyTorch training loop
2. **No pruning** - Efficient KAN doesn't have built-in pruning
3. **Standard PyTorch save/load** - Uses `torch.save()` instead of `saveckpt()`
4. **Manual training loop** - More control but requires more code
5. **Better memory efficiency** - Can handle larger batch sizes

See `KAN_IMPLEMENTATIONS.md` for detailed comparison.

## Output Files

The notebook will create:

- `model/efficient_kan_model_target.pth` - Trained model weights
- `results/efficient_kan_test_metrics.csv` - Performance metrics (if configured)

## Next Steps

After running the notebook:

1. Check training/test loss plots for convergence
2. Review performance metrics (RMSE, MAE, R²)
3. Compare with other model results in `results/`
4. Visualize learned feature relationships using the plot functions

## Getting Help

- Check `KAN_IMPLEMENTATIONS.md` for implementation details
- Review the main project `README.md` for overall context
- Consult the [Efficient KAN repository](https://github.com/Blealtan/efficient-kan) for library-specific questions

## License

This notebook is part of the PFDA programming for data analytics project. Please refer to the main project license and attribution requirements.
