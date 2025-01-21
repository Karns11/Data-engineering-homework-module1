# Module 1 Homework:

### Question 1: Knowing docker tags

Run the command to get information on Docker
`docker --help`

Now run the command to get help on the "docker build" command:
`docker build --help`

Do the same for "docker run".
`docker run --help`

## QUESTION: Which tag has the following text? - Automatically remove the container when it exits

## ANSWER

`docker rm --help`

### Question 2. Understanding docker first run

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash. Now check the python modules that are installed ( use pip list )

## ANSWER

`docker run -it --entrypoint=bash python:3.9`
This returns: wheel 0.43.0

### Question 3. Count records

## QUESTION: How many taxi trips were totally made on September 18th 2019?

`docker network create pg-network-homework`

`docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v "c:/Users/natha/Documents/data-engineering-zoomcamp/2025 Cohort/week_1_basics_n_setup/2_docker_sql/Homeowrk/ny_taxi_postgres_data_homework:/var/lib/postgresql/data" \
    -p 5432:5432 \
    --network=pg-network-homework \
    --name pg-database-homework-main \
    postgres:13
`

Then

`docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network-homework \
    --name pgadmin-homework-main \
    dpage/pgadmin4`

Then

`URL="https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2019-09.parquet"`

Then

`python IngestDataToPostgres.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_trips \
    --url=${URL}`

Then

`URL="https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"`

`python IngestDataToPostgresZones.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=zone_lookup \
    --url=${URL}`

THEN

`select count(*) from green_taxi_trips where lpep_pickup_datetime::date = '2019-09-18' and lpep_dropoff_datetime::date = '2019-09-18'`

## ANSWER

15612

### Question 4. Longest trip for each day

## QUESTION: Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

## ANSWER

`select lpep_pickup_datetime ::date, max(trip_distance) from green_taxi_trips group by lpep_pickup_datetime ::date order by max(trip_distance) desc`

2019-09-26

### Question 5. Three biggest pick up Boroughs

## QUESTION: Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown. Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

`select zl."Borough", sum(tt.total_amount) from green_taxi_trips as tt left join zone_lookup as zl on tt."PULocationID" = zl."LocationID" where tt.lpep_pickup_datetime::date = '2019-09-18' group by zl."Borough" having sum(tt.total_amount) > 50000`

## ANSWER:

"Brooklyn" "Manhattan" "Queens"

### Question 6. Largest tip

## QUESTION: For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

`select zl."Zone", max(tt."tip_amount") from green_taxi_trips as tt left join zone_lookup as zl on tt."DOLocationID" = zl."LocationID" where tt.lpep_pickup_datetime::date between '2019-09-01' and '2019-09-30' and tt."PULocationID" = 7 GROUP BY zl."Zone" ORDER BY max(tt."tip_amount") DESC`

## ANSWER:

JFK Airport

### Question 7. Creating Resources

##QUESTION: Output of terraform apply?

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:

- create

Terraform will perform the following actions:

# google_bigquery_dataset.demo_dataset will be created

- resource "google_bigquery_dataset" "demo_dataset" {

  - creation_time = (known after apply)
  - dataset_id = "demo_dataset"
  - default_collation = (known after apply)
  - delete_contents_on_destroy = false
  - effective_labels = (known after apply)
  - etag = (known after apply)
  - id = (known after apply)
  - is_case_insensitive = (known after apply)
  - last_modified_time = (known after apply)
  - location = "US"
  - max_time_travel_hours = (known after apply)
  - project = "terraform-demo-448420"
  - self_link = (known after apply)
  - storage_billing_model = (known after apply)
  - terraform_labels = (known after apply)

  - access (known after apply)
    }

# google_storage_bucket.demo-bucket will be created

- resource "google_storage_bucket" "demo-bucket" {

  - effective_labels = (known after apply)
  - force_destroy = true
  - id = (known after apply)
  - location = "US"
  - name = "terraform-demo-448420-demo-bucket"
  - project = (known after apply)
  - public_access_prevention = (known after apply)
  - self_link = (known after apply)
  - storage_class = "STANDARD"
  - terraform_labels = (known after apply)
  - uniform_bucket_level_access = (known after apply)
  - url = (known after apply)

  - lifecycle_rule {

    - action {
      - type = "AbortIncompleteMultipartUpload" # (1 unchanged attribute hidden)
        }
    - condition { + age = 1 + matches_prefix = [] + matches_storage_class = [] + matches_suffix = [] + with_state = (known after apply) # (3 unchanged attributes hidden)
      }
      }

  - versioning (known after apply)

  - website (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value:
