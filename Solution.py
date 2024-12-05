# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
data_file = 'your_dataset.csv'  # Replace with your file name
data = pd.read_csv(data_file)

# Step 2: Data exploration
print("\nDataset Head:")
print(data.head())

print("\nDataset Info:")
data.info()

print("\nSummary Statistics:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())