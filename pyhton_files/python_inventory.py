import pandas as pd
from sqlalchemy import create_engine
df1 = pd.read_csv('blinkit_inventory.csv')
df2 = pd.read_csv('blinkit_inventoryNew.csv')
print(df1.head())
print(df2.head())
print(df1.isnull().sum())
print(df2.isnull().sum())
df1.columns = df1.columns.str.lower()
df1.columns=df1.columns.str.replace(" ","_")
df2.columns = df2.columns.str.lower()
df2.columns=df2.columns.str.replace(" ","_")
server = "LAPTOP-D83L8KGR"
database = "blinkit"
connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)
engine = create_engine(connection_string)
df1.to_sql(
    "inventory_old",
    con=engine,
    if_exists="replace",
    index=False
)
df2.to_sql(
    "inventory_new",
    con=engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully!")