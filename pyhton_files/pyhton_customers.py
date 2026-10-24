import pandas as pd
from sqlalchemy import create_engine
df=pd.read_csv('blinkit_customers.csv')
# print(df.head())
print(df.isnull().sum())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
print(df.columns)
#load the data into SQL Server database using SQLAlchemy
server = "LAPTOP-D83L8KGR"
database = "blinkit"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)
engine = create_engine(connection_string)
df.to_sql(
    "customers",
    con=engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully!")
