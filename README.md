### Prerequisites

Project requires works python 3.10.8, pyenv, colima, docker, and poetry.

Install tool to manage python version `pyenv`

#### Install container runtime

```bash
# install docker
brew install docker
brew link docker # optional

# install docker-compose
brew install docker-compose

# install colima container run time
brew install colima
```

#### Preparing

```bash
# Install required python version (defined in pyproject.toml)
pyenv install $(cat .python-version)

# Setup dependencies
python3 -m venv ${PWD}/venv
source ${PWD}/venv/bin/activate
poetry install
```

### Running

```bash
# via docker
colima start
docker compose up -d
```

The application is accessible at <http://localhost:3000>.

### Create tables

1. Connect to the postgresSQL database from the local machine using the url
_localhost://postgres:postgres@postgres:5432/alpas_

2. Run the SQL script in [create_table.sql](scripts/create_table.sql) file located in the db folder

### Insert data in the tables

1. Start the containers
```bash
docker-compose up -d
```
2. Exec into the docker container
```bash
docker-compose run app bash
```
3.Change the working directory to `scripts` directory
```bash
cd scripts
```
4.Run the python command 
```bash
python insert_data.json
```

### Testing

`pytest` will run all unit tests that you specify in your codebase.

As pytest convention, all files matching `test_*.py` will be included.

#### Running tests
```bash
docker-compose run app bash
poetry run pytest -vv tests
```

#### Choice of the database

For storing profit and loss statements of companies with multiple years of data, a relational database is a suitable choice. They offer robust querying capabilities, support for complex data relationships, and transactions to ensure data integrity.

Also, the data is time-series, we can use the relational database with time-series support. Hence, the choice is PostgresSQL (with TimescaleDB extension when the data size increases).

Also, TimescaleDB is optimized for insertion since the update event is very rare.

Comparison on TimescaleDB Vs Mongo for time-series data:
1. 260% higher insertion performance
2. 54 times Faster queries
3. Time oriented analytics functions (such as candle sticks)
4. Stable and tested Postgres database
5. Use PostgresSQl for non time-series data in the same database

#### Scalability of the Database

1. If companies is added to the data
```bash
# Add company table
CREATE TABLE company (company_id SERIAL PRIMARY KEY, company_name VARCHAR(100) NOT NULL);
# Add a column company id and a constraint in the pnl table
company_id INTEGER NOT NULL,
FOREIGN KEY (company_id) REFERENCES company (company_id)
```

2. More data gets added over time
```bash
# Use timescale DB extension with postgresSQL.
# With the TimescaleDB hypertable, we can efficiently store and query the data
# over time. TimescaleDB will also automatically handle data partitioning, compression,
# and indexing to optimize the performance of time-series queries, thus making it suitable for
# managing large volumes of time-stamped data efficiently.

# Change report_date column to type TIMESTAMP.
# specify this column as the time-based dimension that will be used to partition and organize the time-series data efficiently.

#Create a hypertable using TimescaleDB to optimize time-series data storage.
SELECT create_hypertable('pnl', 'report_date');
```

#### Possible future improvements
- Implement Authentication - **DONE**
- Write (more) tests and fix the not working test
- Implement CI/CD Pipeline
- Github hooks for formatting the code
