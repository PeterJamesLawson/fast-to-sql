from datetime import datetime

import pandas as pd

import pyodbc
from fast_to_sql import fast_to_sql as fts

# Test Dataframe for insertion
df = pd.DataFrame({
    "Col1": [1, 2, 3],
    "Col2": ["A", "B", "C"],
    "Col3": [True, False, True],
    "Col4": [datetime(2020,1,1),datetime(2020,1,2),datetime(2020,1,3)]
})

# Create a pyodbc connection
conn = pyodbc.connect(
    """Driver={ODBC Driver 17 for SQL Server};
    Server=localhost;
    Database=test;
    UID=sa;
    PWD=1234567mypass;"""
)

# If a table is created, the generated sql is returned
create_statement = fts.fast_to_sql(df, "testtable5", conn, if_exists="replace", custom={"Col1":"INT PRIMARY KEY"}, temp=False)

# Commit upload actions and close connection
conn.commit()
conn.close()

