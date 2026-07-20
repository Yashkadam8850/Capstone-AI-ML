import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=pd.read_csv("CAPSTONE PROJECT/Data/clean_dataset/googleplaystore_cleaned.csv")
print(data.head(5))
print("The data has been loaded successfully")


# count app in each category 
Top_categories = data ["Category"].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=Top_categories.values,y=Top_categories.index,hue=Top_categories.index,palette="bright",legend=False)
plt.title("Top 10 App Categrories by Number of App")
plt.xlabel("Number of Apps")
plt.ylabel("Category")
plt.grid(axis="x",linestyle="--",alpha=0.8)
plt.show()


Content_Rating=data["Content Rating"].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=Content_Rating,y=Content_Rating.index,hue=Content_Rating.index,palette="flare",legend=False)
plt.title("Content Rating Distribution")
plt.xlabel("Number of Apps")
plt.ylabel("Content Rating")
plt.grid(axis="x",linestyle="--",alpha=0.8)
plt.show()


# Calculate average rating for each category 
avg_rating =(data.groupby("Category")["Rating"].mean().sort_values(ascending=False))
sns.barplot(x=avg_rating.head(15).values,y=avg_rating.head(15).index,hue=avg_rating.head(15).index,palette="viridis")
plt.title("Top 15 Categories by Average Rating", fontsize=14)
plt.xlabel("Average Rating")
plt.ylabel("Category")
plt.grid(axis="x",linestyle="--",alpha=0.8)
plt.show()

#Category vs Total Installs (Horizontal Bar Chart)
category_installs = (data.groupby("Category")["Installs"].sum().sort_values(ascending=False).head(10))

plt.figure(figsize=(10,6))
sns.barplot(x=category_installs.values,y=category_installs.index,hue=category_installs.index,palette="viridis",legend=False)
plt.title("Top 10 Categories by Total Installs")
plt.xlabel("Total Installs")
plt.ylabel("Category")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.show()

#Free vs Paid Apps (Pie Chart)
app_type = data["Type"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(app_type,labels=app_type.index,autopct="%1.1f%%",startangle=90,explode=[0.05,0],)
plt.title("Free vs Paid Apps")
plt.show()

#Rating vs Reviews (Scatter Plot)

plt.figure(figsize=(10,6))
plt.scatter(data["Reviews"],data["Rating"],alpha=0.5)
plt.xscale("log")
plt.title("Rating vs Reviews")
plt.xlabel("Reviews")
plt.ylabel("Rating")
plt.grid(True)
plt.show()

#Reviews vs Installs (Scatter Plot)

plt.figure(figsize=(10,6))

plt.scatter(data["Reviews"],data["Installs"],alpha=0.5)
plt.xscale("log")
plt.yscale("log")
plt.title("Reviews vs Installs")
plt.xlabel("Reviews")
plt.ylabel("Installs")
plt.grid(True)
plt.show()

#Correlation Heatmap

numeric_data = data.select_dtypes(include=["int64","float64"])

corr = numeric_data.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

#Outlier Boxplots

columns = ["Rating","Reviews","Price"]

for col in columns:

    plt.figure(figsize=(10,3))

    sns.boxplot(x=data[col],color="skyblue")

    if col == "Reviews":
        plt.xscale("log")

    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)

    plt.show()
