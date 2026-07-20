import pandas as pd
import sqlite3

data = pd.read_csv("c:/Users/Yash/OneDrive/Desktop/CAPSTONE PROJECT/Data/Part 1/clean_dataset/googleplaystore_cleaned.csv")

Connection=sqlite3.connect("Google_Playstore_Data.db")
data.to_sql(
    "playstore_apps",
    Connection,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")

