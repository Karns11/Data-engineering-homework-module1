# Module 1 Homework:

### Question 1: Understanding docker first run

Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.
`docker run -it --entrypoint=bash python:3.12.8`

## QUESTION: What's the version of pip in the image?

## ANSWER

24.3.1

### Question 2. Understanding Docker networking and docker-compose

Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

## ANSWER

db:5432

# Prepare Postgres....

`docker network create pg-network-2025Module1HW`

`docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v "c:/Users/natha/Documents/data-engineering-zoomcamp/2025 Cohort/week_1_basics_n_setup/Homework/ny_taxi_postgres_data:/var/lib/postgresql/data" \
    -p 5432:5432 \
    --network=pg-network-2025Module1HW \
    --name pg-database-2025Module1HW \
    postgres:13
    `

`docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network-2025Module1HW \
    --name pgadmin-2025Module1HW \
    dpage/pgadmin4
`

##### Connect to pgadmin

`python IngestDataToPostgres.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_trips_hw `

`
python IngestDataToPostgresZones.py \
 --user=root \
 --password=root \
 --host=localhost \
 --port=5432 \
 --db=ny_taxi \
 --table_name=zonesData_hw`

### Question 3. Trip Segmentation Count

## QUESTION: During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, respectively, happened:

## ANSWERS

`select count(*)
from green_taxi_trips_hw
where lpep_dropoff_datetime::date between '2019-10-01' and '2019-10-31'
	and trip_distance >= 1`

104,802

`select count(*)
from green_taxi_trips_hw
where lpep_dropoff_datetime::date between '2019-10-01' and '2019-10-31'
	and trip_distance > 1 and trip_distance <= 3`

198,924

`select count(*)
from green_taxi_trips_hw
where lpep_dropoff_datetime::date between '2019-10-01' and '2019-10-31'
	and trip_distance > 3 and trip_distance <= 7`

109,603

`select count(*)
from green_taxi_trips_hw
where lpep_dropoff_datetime::date between '2019-10-01' and '2019-10-31'
	and trip_distance > 7 and trip_distance <= 10`

27,678

`select count(*)
from green_taxi_trips_hw
where lpep_dropoff_datetime::date between '2019-10-01' and '2019-10-31'
	and trip_distance > 10`

35,189

### Question 4. Longest trip for each day

## QUESTION: Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

## ANSWER

`select lpep_pickup_datetime ::date, max(trip_distance) 
from green_taxi_trips_hw 
group by lpep_pickup_datetime ::date 
order by max(trip_distance) desc`

2019-10-31

### Question 5. Three biggest pick up Boroughs

## QUESTION: Which were the top pickup locations with over 13,000 in total_amount (across all trips) for 2019-10-18? Consider only lpep_pickup_datetime when filtering by date.

`select zl."Zone", sum(tt.total_amount) 
from green_taxi_trips_hw as tt 
left join "zonesData_hw" as zl 
on tt."PULocationID" = zl."LocationID" where tt.lpep_pickup_datetime::date = '2019-10-18' 
group by zl."Zone" 
having sum(tt.total_amount) > 13000`

## ANSWER:

East Harlem North, East Harlem South, Morningside Heights

### Question 6. Largest tip

## QUESTION: For the passengers picked up in October 2019 in the zone named "East Harlem North" which was the drop off zone that had the largest tip?

`select zl."Zone", max(tt."tip_amount") 
from green_taxi_trips_hw as tt 
left join "zonesData_hw" as zl 
on tt."DOLocationID" = zl."LocationID" 
where tt.lpep_pickup_datetime::date between '2019-10-01' and '2019-10-31' and tt."PULocationID" = 74 
GROUP BY zl."Zone" 
ORDER BY max(tt."tip_amount") DESC`

## ANSWER:

JFK Airport

### Question 7. Terraform Workflow

## QUESTION: Which of the following sequences, respectively, describes the workflow for:

Downloading the provider plugins and setting up backend,
Generating proposed changes and auto-executing the plan
Remove all resources managed by terraform`

## ANSWER:

terraform init, terraform apply -auto-approve, terraform destroy
