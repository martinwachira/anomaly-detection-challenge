import pandas as pd
import numpy as np

dataset = pd.read_csv('~/anomalies/anomalies1.csv', parse_dates=[10])

# Printing head of the DataFrame
print(dataset.head())