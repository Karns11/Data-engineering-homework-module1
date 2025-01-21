import pandas as pd

from sqlalchemy import create_engine

import argparse

import os

import pyarrow
import fastparquet



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    

    csv_name = 'output.parquet'

    os.system(f"wget {url} -O {csv_name}")

    
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    engine.connect()

    df = pd.read_csv(csv_name)

    # df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    # df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

    df.to_sql(name=table_name, con=engine, if_exists="append")

    print("data saved to db successfully")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to postgres')

    # user, password, host, port, db name, table name, url of the csv

    parser.add_argument('--user', help='user name for postgres') 
    parser.add_argument('--password', help='password for postgres') 
    parser.add_argument('--host', help='host for postgres') 
    parser.add_argument('--port', help='port for postgres') 
    parser.add_argument('--db', help='database name for postgres') 
    parser.add_argument('--table_name', help='name of the table we will write the results to') 
    parser.add_argument('--url', help='url of the csv') 


    args = parser.parse_args()

    main(args)



