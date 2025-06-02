from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')

try:
    accounts = pd.read_csv('data/accounts.csv')
    devices = pd.read_csv('data/devices.csv')
    merchants = pd.read_csv('data/merchants.csv')
    transaction = pd.read_csv('data/transaction.csv')
except FileNotFoundError as e:
    print(f"CSV file not found: {e}")
    exit()

property_table = [
    ('Accounts', accounts),
    ('Devices', devices),
    ('Merchant', merchants),
    ('Transaction', transaction)
]

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(connection_string)

for table_name, df in property_table:
    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        print(f"Inserted into {table_name} successfully.")
    except SQLAlchemyError as e:
        print(f"Error inserting into {table_name}: {e}")
        engine.dispose()
        break  

print("Script completed.")
