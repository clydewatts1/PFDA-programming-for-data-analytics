"""
Simplified Temporal KAN (TKAN) Implementation
Using PyTorch with temporal encoding
"""

import torch
import torch.nn as nn
import numpy as np
import math


class TemporalEncoding(nn.Module):
    """Sinusoidal temporal encoding"""
    def __init__(self, d_model=16):
        super().__init__()
        self.d_model = d_model
        
    def forward(self, hour, day_of_week, day_of_year, month):
        batch_size = hour.shape[0]
        device = hour.device
        
        # Normalize to [0, 2*pi]
        hour_norm = (hour / 24.0) * 2 * math.pi
        dow_norm = (day_of_week / 7.0) * 2 * math.pi
        doy_norm = (day_of_year / 365.0) * 2 * math.pi
        month_norm = ((month - 1) / 12.0) * 2 * math.pi
        
        # Sinusoidal encoding
        encodings = []
        for t in [hour_norm, dow_norm, doy_norm, month_norm]:
            for i in range(self.d_model // 8):
                freq = 2 ** i
                encodings.append(torch.sin(freq * t))
                encodings.append(torch.cos(freq * t))
        
        return torch.stack(encodings, dim=1)


class TKANLayer(nn.Module):
    """Temporal KAN Layer with learnable activation"""
    def __init__(self, in_dim, out_dim, grid_size=5, use_temporal=True, temporal_dim=16):
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.grid_size = grid_size
        self.use_temporal = use_temporal
        self.temporal_dim = temporal_dim if use_temporal else 0
        
        total_in = in_dim + self.temporal_dim
        
        # Learnable weights for each input feature
        self.weight = nn.Parameter(torch.randn(out_dim, total_in, grid_size) * 0.1)
        self.bias = nn.Parameter(torch.zeros(out_dim))
        
        # Grid points
        self.register_buffer('grid', torch.linspace(-2, 2, grid_size))
        
        # Temporal encoder
        if use_temporal:
            self.temporal_encoder = TemporalEncoding(d_model=temporal_dim)
    
    def forward(self, x, temporal_features=None):
        batch_size = x.size(0)
        
        # Add temporal encoding
        if self.use_temporal and temporal_features is not None:
            temporal_enc = self.temporal_encoder(
                temporal_features['hour'],
                temporal_features['day_of_week'],
                temporal_features['day_of_year'],
                temporal_features['month']
            )
            x = torch.cat([x, temporal_enc], dim=1)
        
        # x: (batch, total_in)
        # Compute output for each grid point
        # weight: (out_dim, total_in, grid_size)
        x_norm = torch.tanh(x)  # (batch, total_in)
        
        # Compute distance to each grid point
        # x_norm: (batch, total_in, 1)
        # grid: (grid_size,)
        x_expanded = x_norm.unsqueeze(-1)  # (batch, total_in, 1)
        grid_expanded = self.grid.unsqueeze(0).unsqueeze(0)  # (1, 1, grid_size)
        
        # RBF kernel
        distances = (x_expanded - grid_expanded) ** 2  # (batch, total_in, grid_size)
        rbf = torch.exp(-distances)  # (batch, total_in, grid_size)
        
        # Apply weights
        # rbf: (batch, total_in, grid_size)
        # weight: (out_dim, total_in, grid_size)
        output = torch.einsum('big,oig->bo', rbf, self.weight) + self.bias
        
        return output
    
    def regularization_loss(self):
        return torch.mean(torch.abs(self.weight))


class TKAN(nn.Module):
    """Complete TKAN network"""
    def __init__(self, layers_hidden, grid_size=5, use_temporal=True, temporal_dim=16):
        super().__init__()
        self.layers = nn.ModuleList()
        self.use_temporal = use_temporal
        
        for i in range(len(layers_hidden) - 1):
            use_temp = use_temporal if i == 0 else False
            self.layers.append(
                TKANLayer(
                    layers_hidden[i],
                    layers_hidden[i + 1],
                    grid_size=grid_size,
                    use_temporal=use_temp,
                    temporal_dim=temporal_dim
                )
            )
    
    def forward(self, x, temporal_features=None):
        for i, layer in enumerate(self.layers):
            temp_feat = temporal_features if i == 0 and self.use_temporal else None
            x = layer(x, temp_feat)
        return x
    
    def regularization_loss(self):
        return sum(layer.regularization_loss() for layer in self.layers)


def extract_temporal_features(df, datetime_col='DateTime'):
    """Extract temporal features from DataFrame"""
    import pandas as pd
    
    if not pd.api.types.is_datetime64_any_dtype(df[datetime_col]):
        df[datetime_col] = pd.to_datetime(df[datetime_col])
    
    return {
        'hour': torch.tensor(df[datetime_col].dt.hour.values, dtype=torch.float32),
        'day_of_week': torch.tensor(df[datetime_col].dt.dayofweek.values, dtype=torch.float32),
        'day_of_year': torch.tensor(df[datetime_col].dt.dayofyear.values, dtype=torch.float32),
        'month': torch.tensor(df[datetime_col].dt.month.values, dtype=torch.float32)
    }


if __name__ == "__main__":
    print("Testing Simplified TKAN...")
    
    # Test model
    model = TKAN(layers_hidden=[10, 20, 1], grid_size=5, use_temporal=True, temporal_dim=16)
    
    # Dummy data
    batch_size = 32
    x = torch.randn(batch_size, 10)
    
    temporal_features = {
        'hour': torch.randint(0, 24, (batch_size,)).float(),
        'day_of_week': torch.randint(0, 7, (batch_size,)).float(),
        'day_of_year': torch.randint(0, 365, (batch_size,)).float(),
        'month': torch.randint(1, 13, (batch_size,)).float()
    }
    
    # Forward pass
    output = model(x, temporal_features)
    print(f"✓ Input shape: {x.shape}")
    print(f"✓ Output shape: {output.shape}")
    print(f"✓ Regularization loss: {model.regularization_loss():.4f}")
    
    # Test without temporal
    model_no_temp = TKAN(layers_hidden=[10, 20, 1], grid_size=5, use_temporal=False)
    output_no_temp = model_no_temp(x)
    print(f"✓ Output shape (no temporal): {output_no_temp.shape}")
    
    print("\n✅ All tests passed!")
