import pandas as pd
## Data Loading and Basic Inspection

data = pd.read_csv("Desktop/CAPSTONE PROJECT/Part 1/Data/Raw/googleplaystore.csv")
print("The data has been loaded successfully")


print("="*55)
print("Data Information")
print(data.info())
print("="*55)
print("Data Describe")
print(data.describe())
print("="*55)
print("Data shape")
print(data.shape)
print("="*55)
print("Columns ")
print(data.columns)
print("="*55)
print("Data Type")
print(data.dtypes)
print("="*55)
print("Missing values")
print(data.isnull().sum())
print("="*55)
print("Duplicate values")
print(data.duplicated().sum())


# drop null values

data_cleaned = data.dropna()
print("Shape after dropping null values:", data_cleaned.shape)
print("Missing values after dropping nulls:")
print(data_cleaned.isnull().sum())

data_cleaned = data_cleaned.drop_duplicates()
print("Shape after dropping duplicate values:", data_cleaned.shape)
print("Duplicate values after dropping duplicates:")
print(data_cleaned.duplicated().sum())
print("Data after cleaning:")

### Removing 'Varies with device' from "Android Ver" "size" and "Current Ver"

columns_to_clean = ['Android Ver', 'Size', 'Current Ver']

for col in columns_to_clean:
    if col in data_cleaned.columns:
        initial_count = data_cleaned[data_cleaned[col] == 'Varies with device'].shape[0]
        print(f"Initial count of 'Varies with device' in '{col}': {initial_count}")

        # Filter out rows where the current column has 'Varies with device'
        data_cleaned = data_cleaned[data_cleaned[col] != 'Varies with device'].copy()

        print(f"Shape after dropping 'Varies with device' from '{col}':", data_cleaned.shape)
        print(f"Count of 'Varies with device' in '{col}' after dropping:", data_cleaned[data_cleaned[col] == 'Varies with device'].shape[0])

# Drop the 'Current Ver' and 'Android Ver' columns
data_cleaned = data_cleaned.drop(columns=['Current Ver', 'Android Ver'])

print("DataFrame after dropping 'Current Ver' and 'Android Ver':")
print(data_cleaned.head())
# Drop the 'Genres' column
data_cleaned = data_cleaned.drop(columns=["Genres"])

print(data_cleaned.head())
# Save the cleaned DataFrame to a new CSV file
data_cleaned.to_csv('googleplaystore_cleaned.csv', index=False)

print("Cleaned data saved to 'googleplaystore_cleaned.csv'")
