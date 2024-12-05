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

# Step 3: Basic Data Analysis
# Example: Correlation between numerical columns (if applicable)
if not data.select_dtypes(include='number').empty:
    print("\nCorrelation Matrix:")
    print(data.corr())
    
# Step 4: Visualizations
# Histogram of a numeric column (replace 'column_name' with an actual column)
if 'column_name' in data.columns:
    plt.figure(figsize=(8, 6))
    data['column_name'].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram of Column Name')
    plt.xlabel('Column Name')
    plt.ylabel('Frequency')
    plt.show()


# Scatter plot of two numeric columns (replace 'x_column' and 'y_column')
if {'x_column', 'y_column'}.issubset(data.columns):
    plt.figure(figsize=(8, 6))
    plt.scatter(data['x_column'], data['y_column'], alpha=0.7, color='green')
    plt.title('Scatter Plot of X vs Y')
    plt.xlabel('X Column')
    plt.ylabel('Y Column')
    plt.show()


# Bar plot of a categorical column (replace 'categorical_column')
if 'categorical_column' in data.columns:
    plt.figure(figsize=(10, 6))
    data['categorical_column'].value_counts().plot(kind='bar', color='orange', edgecolor='black')
    plt.title('Bar Plot of Categorical Column')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.show()
    

# Step 5: Findings or Observations
# Print any insights you notice in the dataset or visualizations
print("\nObservations:")
print("1. Add your observations here.")
print("2. Replace this text with meaningful insights.")
