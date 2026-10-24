import pandas as pd
from sqlalchemy import create_engine
df = pd.read_excel('Blinkit_Delivery_salary.xlsx')
# print(df.head())
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
server = "LAPTOP-D83L8KGR"
database = "blinkit"
connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)
engine = create_engine(connection_string)
df.to_sql(
    "salarys",
    con=engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully!")