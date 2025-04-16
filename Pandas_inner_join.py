import pandas as pd
from sqlalchemy import create_engine

# Create a database engine (replace with your database URL)
# Example: 'sqlite:///Chinook.sqlite' for SQLite
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
    engine
)

# Print head of DataFrame
print(df.head())