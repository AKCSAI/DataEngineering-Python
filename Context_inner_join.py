import pandas as pd
from sqlalchemy import create_engine

# Create a database engine (replace with your database URL)
# Example: 'sqlite:///example.db' for SQLite or 'postgresql://user:password@localhost/dbname' for PostgreSQL
engine = create_engine('sqlite:///example.db')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())