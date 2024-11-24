import sqlite3
from pybaseball import batting_stats, pitching_stats, fielding_stats
import pandas as pd

def connect_to_database(db_name):
    """
    Establishes a connection to the SQLite database.
    """
    return sqlite3.connect(db_name)

def create_table_from_dataframe(table_name, dataframe, connection):
    """
    Dynamically creates a table in SQLite based on a pandas DataFrame's structure.
    """
    cursor = connection.cursor()

    # Escape column names by wrapping them in double quotes
    column_definitions = ', '.join([f'"{col}" TEXT' for col in dataframe.columns])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
    cursor.execute(create_table_sql)
    connection.commit()

    print(f"Table '{table_name}' created/validated with columns: {', '.join(dataframe.columns)}")

def fetch_and_store_data(table_name, fetch_function, connection, year):
    """
    Fetches data using a pybaseball function, dynamically creates a SQLite table,
    and inserts all columns into the database.
    """
    print(f"Fetching data for {table_name} in {year}...")
    try:
        # Fetch data for the given year
        data = fetch_function(year)

        # Handle empty DataFrames
        if data.empty:
            print(f"No data returned for {table_name} in {year}. Skipping.")
            return

        # Convert all data to strings to ensure compatibility with SQLite
        data = data.astype(str)

        # Create table dynamically based on DataFrame structure
        create_table_from_dataframe(table_name, data, connection)

        # Insert the data into SQLite
        data.to_sql(table_name, connection, if_exists='append', index=False)
        print(f"Data for {table_name} in {year} saved successfully.")

    except Exception as e:
        print(f"Error fetching or saving data for {table_name} in {year}: {e}")

def main():
    db_name = 'baseball-dump.db'
    conn = connect_to_database(db_name)

    # Define the range of years to fetch data for
    years = range(2015, 2024)  # From 2015 to 2023

    # Define datasets to fetch: table name and corresponding pybaseball function
    datasets = [
        ('batting_stats', batting_stats),    # Batting stats from FanGraphs
        ('pitching_stats', pitching_stats),  # Pitching stats from FanGraphs
        ('fielding_stats', fielding_stats)   # Fielding stats from FanGraphs
    ]

    # Fetch and store each dataset for all years
    for year in years:
        for table_name, fetch_function in datasets:
            fetch_and_store_data(table_name, fetch_function, conn, year)

    conn.close()
    print("All datasets fetched and stored successfully!")

if __name__ == "__main__":
    main()
