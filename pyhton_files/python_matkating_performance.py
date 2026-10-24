import pandas as pd
from sqlalchemy import create_engine
df=pd.read_csv('blinkit_marketing_performance.csv')
# print(df.head())
print(df.isnull().sum())
df.columns = df.columns.str.lower() # convert column names to lower case
df.columns = df.columns.str.replace(' ', '_') # replace spaces with underscores
print(df.columns)
server = "LAPTOP-D83L8KGR"
database = "blinkit"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)
engine = create_engine(connection_string)
df.to_sql(
    "marketing_performance",
    con=engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully!")
