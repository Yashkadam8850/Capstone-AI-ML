import pandas as pd
import sqlite3
Connection=sqlite3.connect("Google_Playstore_Data.db")

# Query 1 - Display first 10 rows
query1 = """
SELECT *
FROM playstore_apps
LIMIT 10;
"""

# Query 2 - Number of apps in each category
query2 = """
SELECT Category,
       COUNT(*) AS TOTAL_APPS
FROM playstore_apps
GROUP BY Category
ORDER BY TOTAL_APPS DESC;
"""

# Query 3 - Total number of apps
query3 = """
SELECT COUNT(*) AS TOTAL_APPS
FROM playstore_apps;
"""

# Query 4 - Average rating by category
query4 = """
SELECT Category,
       ROUND(AVG(Rating), 2) AS Average_Rating
FROM playstore_apps
GROUP BY Category
ORDER BY Average_Rating DESC;
"""

# Query 5 - Top 10 most reviewed apps
query5 = """
SELECT App,
       Reviews
FROM playstore_apps
ORDER BY Reviews DESC
LIMIT 10;
"""

# Query 6 - Free vs Paid apps
query6 = """
SELECT Type,
       COUNT(*) AS TOTAL_APPS
FROM playstore_apps
GROUP BY Type;
"""

# Query 7 - Apps with rating greater than 4.5
query7 = """
SELECT App,
       Rating
FROM playstore_apps
WHERE Rating > 4.5
ORDER BY Rating DESC;
"""

# Query 8 - Content rating distribution
query8 = """
SELECT "Content Rating",
       COUNT(*) AS TOTAL_APPS
FROM playstore_apps
GROUP BY "Content Rating"
ORDER BY TOTAL_APPS DESC;
"""

# Query 9 - Apps with more than 1 million reviews
query9 = """
SELECT App,
       Reviews
FROM playstore_apps
WHERE Reviews > 1000000;
"""

# Query 10 - Maximum rating
query10 = """
SELECT MAX(Rating) AS HIGHEST_RATING
FROM playstore_apps;
"""

# Query 11 - Minimum rating
query11 = """
SELECT MIN(Rating) AS LOWEST_RATING
FROM playstore_apps;
"""

# Query 12 - Number of apps in each genre
query12 = """
SELECT Genres,
       COUNT(*) AS TOTAL_APPS
FROM playstore_apps
GROUP BY Genres
ORDER BY TOTAL_APPS DESC;
"""

# Query 13 - Top 10 categories by average installs
query13 = """
SELECT Category,
       ROUND(AVG(Installs), 0) AS AVERAGE_INSTALLS
FROM playstore_apps
GROUP BY Category
ORDER BY AVERAGE_INSTALLS DESC
LIMIT 10;
"""

# Query 14 - Find duplicate app names
query14 = """
SELECT App,
       COUNT(*) AS DUPLICATE_COUNT
FROM playstore_apps
GROUP BY App
HAVING COUNT(*) > 1;
"""

# Query 15 - Categories containing 'GAME'
query15 = """
SELECT DISTINCT Category
FROM playstore_apps
WHERE Category LIKE '%GAME%';
"""
# Store all queries in a dictionary
queries = {
    "Query 1 - First 10 Apps": query1,
    "Query 2 - Apps by Category": query2,
    "Query 3 - Total Apps": query3,
    "Query 4 - Average Rating by Category": query4,
    "Query 5 - Top 10 Most Reviewed Apps": query5,
    "Query 6 - Free vs Paid Apps": query6,
    "Query 7 - Apps with Rating > 4.5": query7,
    "Query 8 - Content Rating Distribution": query8,
    "Query 9 - Apps with More Than 1M Reviews": query9,
    "Query 10 - Highest Rating": query10,
    "Query 11 - Lowest Rating": query11,
    "Query 12 - Apps by Genre": query12,
    "Query 13 - Top Categories by Average Installs": query13,
    "Query 14 - Duplicate App Names": query14,
    "Query 15 - Categories Containing 'GAME'": query15
}

# Execute and print each query
for title, sql in queries.items():
    print(f"\n{'=' * 60}")
    print(title)
    print(f"{'=' * 60}")

    result = pd.read_sql_query(sql, Connection)
    print(result)