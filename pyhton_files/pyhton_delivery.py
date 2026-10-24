import pandas as pd
from sqlalchemy import create_engine
df=pd.read_csv('blinkit_delivery_performance.csv')
# print(df.head())
print(df.isnull().sum())
df['reasons_if_delayed'] =df['reasons_if_delayed'].fillna('No Delay') # fill null values with 'No Delay'
print(df.isnull().sum())
df=df.rename(columns={'reasons_if_delayed':'delay_reasons'}) # rename column
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
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
    "delivery_performance",
    con=engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully!")