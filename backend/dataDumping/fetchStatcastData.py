import sqlite3
from pybaseball import statcast
import pandas as pd
from datetime import datetime

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

def fetch_and_store_statcast_data(connection, start_date, end_date):
    """
    Fetches Statcast data for a given date range and stores it in the database.
    """
    print(f"Fetching Statcast data from {start_date} to {end_date}...")
    try:
        # Fetch Statcast data
        data = statcast(start_date, end_date)

        # Handle empty DataFrames
        if data.empty:
            print(f"No data returned for Statcast from {start_date} to {end_date}. Skipping.")
            return

        # Convert all data to strings to ensure compatibility with SQLite
        data = data.astype(str)

        # Create the table dynamically based on DataFrame structure
        create_table_from_dataframe("statcast", data, connection)

        # Insert the data into SQLite
        data.to_sql("statcast", connection, if_exists='append', index=False)
        print(f"Data from {start_date} to {end_date} saved successfully.")

    except Exception as e:
        print(f"Error fetching or saving Statcast data for {start_date} to {end_date}: {e}")

def generate_date_ranges(start_year, end_year, chunk_size=30):
    """
    Generates date ranges for Statcast queries, broken into manageable chunks.
    """
    date_ranges = []
    for year in range(start_year, end_year + 1):
        start_date = datetime(year, 4, 1)  # Start of MLB season
        end_date = datetime(year, 10, 1)  # End of MLB regular season

        # Break the range into smaller chunks
        current_date = start_date
        while current_date < end_date:
            chunk_end_date = min(current_date + pd.Timedelta(days=chunk_size), end_date)
            date_ranges.append((current_date.strftime('%Y-%m-%d'), chunk_end_date.strftime('%Y-%m-%d')))
            current_date = chunk_end_date + pd.Timedelta(days=1)
    
    return date_ranges

def main():
    db_name = "baseball-dump.db"
    conn = connect_to_database(db_name)

    # Define the range of years for Statcast data
    start_year = 2015
    end_year = datetime.now().year

    # Generate date ranges for fetching data
    date_ranges = generate_date_ranges(start_year, end_year)

    # Fetch and store data for each date range
    for start_date, end_date in date_ranges:
        fetch_and_store_statcast_data(conn, start_date, end_date)

    conn.close()
    print("All Statcast data fetched and stored successfully!")

if __name__ == "__main__":
    main()
