import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
    print("GPU is available:", torch.cuda.get_device_name(0))
else:
    print("GPU is not available.")