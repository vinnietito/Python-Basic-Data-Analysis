# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Replace with your dataset file path
    data_file = 'iris.csv'  # Example dataset, replace with your own
    data = pd.read_csv(data_file)
    print("\nDataset successfully loaded.")
except FileNotFoundError:
    print(f"Error: The file '{data_file}' was not found. Please check the file path.")
    exit()

# Display the first few rows
print("\nDataset Head:")
print(data.head())

# Explore the structure of the dataset
print("\nDataset Info:")
data.info()

print("\nMissing Values:")
print(data.isnull().sum())

# Clean the dataset (fill or drop missing values)
data = data.dropna()  # Dropping missing values (modify as needed)
print("\nAfter Cleaning - Missing Values:")
print(data.isnull().sum())

# Task 2: Basic Data Analysis
print("\nSummary Statistics:")
print(data.describe())

# Example grouping: Replace 'species' and 'sepal_length' with relevant columns
if 'species' in data.columns and 'sepal_length' in data.columns:
    grouped_data = data.groupby('species')['sepal_length'].mean()
    print("\nGrouped Data (Mean Sepal Length by Species):")
    print(grouped_data)

# Task 3: Data Visualization
# Line Chart: Replace 'x_column' and 'y_column' with actual time-series columns
if {'x_column', 'y_column'}.issubset(data.columns):
    plt.figure(figsize=(8, 6))
    plt.plot(data['x_column'], data['y_column'], marker='o', label='Trend')
    plt.title('Line Chart of X Column vs. Y Column')
    plt.xlabel('X Column')
    plt.ylabel('Y Column')
    plt.legend()
    plt.show()

# Bar Chart: Replace 'categorical_column' and 'numerical_column'
if 'species' in data.columns and 'sepal_length' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(x='species', y='sepal_length', data=data, palette='viridis')
    plt.title('Bar Chart: Average Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Sepal Length')
    plt.show()

# Histogram: Replace 'column_name' with a numerical column
if 'sepal_length' in data.columns:
    plt.figure(figsize=(8, 6))
    data['sepal_length'].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram of Sepal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Frequency')
    plt.show()

# Scatter Plot: Replace 'x_column' and 'y_column'
if {'sepal_length', 'petal_length'}.issubset(data.columns):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal_length', y='petal_length', data=data, hue='species', palette='muted')
    plt.title('Scatter Plot: Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.legend(title='Species')
    plt.show()

# Observations
print("\nObservations:")
print("1. Grouping by species reveals differences in average sepal length.")
print("2. The scatter plot shows a positive correlation between sepal length and petal length.")
print("3. The histogram indicates the distribution of sepal lengths is right-skewed.")
print("4. Line chart trends are time-dependent (ensure proper columns).")

