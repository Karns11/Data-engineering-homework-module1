FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow fastparquet

WORKDIR /app
COPY IngestDataToPostgres.py IngestDataToPostgres.py
#COPY output.csv output.csv

ENTRYPOINT ["python", "IngestDataToPostgres.py"]