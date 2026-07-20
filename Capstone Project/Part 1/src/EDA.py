import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("c:/Users/Yash/OneDrive/Desktop/CAPSTONE PROJECT/Data/Part 1/clean_dataset/googleplaystore_cleaned.csv")

## Distribution of App Ratings
app_rating=data["Rating"].describe()
## Number of Apps in Each Category
app_category=data["Category"].value_counts()
## Free vs Paid Apps
type_of_apps=data["Type"].value_counts()
## content rating of apps 
content_ranting =data["Content Rating"].value_counts()

## Rating vs Reviews
rating_reviews= data["Installs"],data["Rating"]
## Category vs Average Rating
avg_rating_category=data.groupby("Category")["Rating"].mean().sort_values()
## category vs Type (Free and paid)
type_category=data.groupby("Category")["Type"].value_counts()
## Category vs Total Intalls
Category_installs=data.groupby("Category")["Installs"].sum()


columns = ["Rating", "Price", "Reviews"]

data[columns] = data[columns].astype(float)

# Top 10 Apps with the most Reviews
Top_10_Apps= data[["App","Reviews","Rating"]].sort_values(by="Reviews",ascending=False).head(10)

# Top 50 App Information 
appinfo= data.groupby("App")[["Reviews","Rating"]].mean().sort_values(by="Reviews",ascending=False).head(50)

#Convert the `Last Updated` column from the format **`Month Day, Year`**
data["Last Updated"]= pd.to_datetime(data['Last Updated'])
data["Last Updated"] = data["Last Updated"].dt.strftime("%m/%d/%Y")

# Size Column Data Type Conversion

data ["Size"] = data ["Size"].replace("M","",regex=False)
data ["Size"] = data["Size"].replace("K","",regex=False)

Install_Info = (data.groupby("App")[["Size", "Installs"]].first().sort_values(by="Installs", ascending=False))


Content_Rating=data.groupby("App")[["Type","Content Rating"]].value_counts().head(50)


def print_section(title):
    """Print a formatted section title."""
    print("\n" + "=" * 80)
    print(title.upper())
    print("=" * 80)


def print_results():
    """Display all analysis results."""

    print("=" * 80)
    print("GOOGLE PLAY STORE DATA ANALYSIS REPORT")
    print("=" * 80)

    reports = [
        ("First 5 Rows", data.head()),
        ("Dataset Information", None),
        ("Statistical Summary", data.describe()),
        ("Dataset Shape", data.shape),
        ("Missing Values", data.isnull().sum()),
        ("Distribution of App Ratings", app_rating),
        ("Number of Apps in Each Category", app_category),
        ("Free vs Paid Apps", type_of_apps),
        ("Content Rating Distribution", content_ranting),
        ("Rating vs Reviews", rating_reviews),
        ("Category vs Average Rating", avg_rating_category),
        ("Category vs Type (Free & Paid)", type_category),
        ("Category vs Total Installs", Category_installs),
        ("Top 10 Apps with Most Reviews", Top_10_Apps),
        ("Top 50 App Information", appinfo),
        ("Install Information", Install_Info),
        ("Content Rating Summary", Content_Rating),
    ]

    for title, result in reports:
        print_section(title)

        if title == "Dataset Information":
            data.info()
        else:
            print(result)

    print("\n" + "=" * 80)
    print("REPORT COMPLETED SUCCESSFULLY")
    print("=" * 80)


if __name__ == "__main__":
    print_results()
