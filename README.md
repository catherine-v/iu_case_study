# IU Case Study

## Project overview

All source code resides in the `src` folder. ETL pipeline defined in `main.py` consists of two isolated steps:

- data extraction from the public openfoddfacts API -- `extract.py`
- load of the extracted data into a database -- `load.py`

All Python requirements are listed in `requirements.txt` file.

List of product ids to import as provided in the case study is made a default option, but can be overwritten with `--product_ids` argument of the `main.py` script, where ids should be represented as a comma-separated string.

The second argument defined by the main pipeline script is the connection string to a database `--conn_str`. It's default value is set to connect to the Docker-run PostgreSQL database.

### Data Extraction

An official Python SKD of openfoodfacts in used to communicate with the API. 

Simple data validation is done using [pydantic](https://docs.pydantic.dev/latest/). When API response does not pass the validation, it is being reported to the logger with ERROR level, and the process continues to the next product.


### Data Load

PostgreSQL database is used to ingest the data. Coonection to the database is established via [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), table structure is defined using the same library.

Since transformation step is limited to 2 column rename operations, is has not been extracted to an independent script.

Data transformation and insert into the table is done using [pandas](https://pandas.pydata.org/docs/index.html).

## Run ETL pipeline

Database and ETL pipeline are configured to run using Docker.

Execute following command to start the database, build a docker container and run the pipeline (docker and docker-composed should be installed on the host machine):

```bash
docker-compose run --build etl
```

After the ETL pipeline finishes, container of the database will remain running to check data in the database. Connection to the database is possible with following credentials:
- host: localhost
- port: 5432
- username: example
- password: example
- database: example
- schema: public

## Potential improvements:

- Unit tests
- Validation improvements based on actual requirements, e.g. every product should have a non-empty name
- Data insert improvements based on actual requiremnents, e.g. using MERGE strategy instead of APPEND, which will fail if the current pipeline runs for the second time (or more)
- Insert performance improvements based on data volume that has to be processed with every run
- ...
