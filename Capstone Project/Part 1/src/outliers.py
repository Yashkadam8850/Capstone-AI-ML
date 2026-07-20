import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("CAPSTONE PROJECT/Data/Part 1/clean_dataset/googleplaystore_cleaned.csv")

# Numeric columns to check
columns = ["Rating", "Reviews", "Price",]

for col in columns:
    # Calculate Quartiles
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1

    # Calculate Limits
    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    # Find Outliers
    outliers = data[(data[col] < lower_limit) | (data[col] > upper_limit)]

    # Print Results
    print("\n" + "=" * 60)
    print(f"Column: {col}")
    print(f"Lower Limit: {lower_limit}")
    print(f"Upper Limit: {upper_limit}")
    print(f"Number of Outliers: {len(outliers)}")
    print(outliers[["App", col]].head(10))

    # Plot
    plt.figure(figsize=(10, 2.5))
    sns.boxplot(x=data[col], color="skyblue")

    # Highlight outliers
    plt.scatter(
        outliers[col],
        [0] * len(outliers),
        color="red",
        s=20,
        label="Outliers"
    )

    plt.title(f"Boxplot of {col} with Outliers")
    plt.xlabel(col)

    # Use log scale only for Reviews
    if col == "Reviews":
        plt.xscale("log")

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


    Q1 = data["Reviews"].quantile(0.25)
Q3 = data["Reviews"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

data["Reviews"] = data["Reviews"].clip(lower=lower_limit, upper=upper_limit)


plt.figure(figsize=(10, 3))
sns.boxplot(x=data["Reviews"])
plt.xscale("log")
plt.title("Reviews After Outlier Capping")
plt.show()

# Select numeric columns
numeric_data = data.select_dtypes(include=["int64", "float64"])

# Correlation matrix
corr = numeric_data.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Matrix")
plt.show()
