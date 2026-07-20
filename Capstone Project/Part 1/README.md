# Capstone Project – Part 1: Google Play Store Data Analysis

This project performs an end-to-end exploratory data analysis (EDA) on the **Google Play Store Apps** dataset — covering data cleaning, outlier detection, SQL-based querying, and visualization.

## Project Structure

```
Capstone Project/Part 1/
├── Data/
│   ├── Raw/
│   │   └── googleplaystore.csv          # Original, unprocessed dataset
│   └── clean_dataset/
│       └── googleplaystore_cleaned.csv  # Cleaned dataset used for analysis
├── src/
│   ├── Data_loading_and_Cleaning.py     # Loads raw data, inspects, cleans, and exports cleaned CSV
│   ├── EDA.py                           # Exploratory data analysis and summary report
│   ├── outliers.py                      # IQR-based outlier detection and capping
│   ├── database.py                      # Loads cleaned data into a SQLite database
│   ├── sql_queries.py                   # 15 SQL queries run against the SQLite database
│   └── visualization.py                 # Matplotlib/Seaborn charts (bar, pie, scatter, heatmap)
├── Visualization/                       # Exported chart images (category counts, ratings, correlations, etc.)
├── Google_Playstore_Data.db             # SQLite database generated from the cleaned dataset
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

The dataset (`googleplaystore.csv`) contains ~10,841 records of Google Play Store apps with attributes including:

`App`, `Category`, `Rating`, `Reviews`, `Size`, `Installs`, `Type`, `Price`, `Content Rating`, `Genres`, `Last Updated`, `Current Ver`, `Android Ver`

## Workflow

1. **Data Loading & Cleaning** (`Data_loading_and_Cleaning.py`)
   - Loads the raw CSV and inspects shape, dtypes, missing values, and duplicates
   - Drops null values and duplicate rows
   - Removes rows with `"Varies with device"` in `Android Ver`, `Size`, and `Current Ver`
   - Drops the `Current Ver`, `Android Ver`, and `Genres` columns
   - Exports the result to `googleplaystore_cleaned.csv`

2. **Exploratory Data Analysis** (`EDA.py`)
   - Rating distribution, app counts per category, free vs. paid split, content rating breakdown
   - Category-level average rating and total installs
   - Top apps by review count, install info, and a full formatted console report

3. **Outlier Detection** (`outliers.py`)
   - IQR-based outlier detection for `Rating`, `Reviews`, and `Price`
   - Caps extreme `Reviews` values and visualizes before/after with boxplots
   - Generates a correlation heatmap of numeric features

4. **Database & SQL Queries** (`database.py`, `sql_queries.py`)
   - Loads the cleaned dataset into a SQLite database (`Google_Playstore_Data.db`), table `playstore_apps`
   - Runs 15 SQL queries covering category counts, average ratings, top reviewed apps, install averages, duplicates, and more

5. **Visualization** (`visualization.py`)
   - Top categories by app count and by average rating
   - Content rating distribution, free vs. paid pie chart
   - Rating vs. Reviews and Reviews vs. Installs scatter plots (log scale)
   - Correlation heatmap and outlier boxplots

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Run the scripts in order from the `src/` directory:

```bash
python src/Data_loading_and_Cleaning.py
python src/EDA.py
python src/outliers.py
python src/database.py
python src/sql_queries.py
python src/visualization.py
```

## Author

Yash Kadam
