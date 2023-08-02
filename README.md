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

Your application will be accessible at <http://localhost:3000>.


### Create tables

1. Exec into the docker container and connect to the database from container using the url
_postgres://postgres:postgres@postgres:5432/alpas_

2. Run the SQL script in [create_table.sql](scripts/create_table.sql) file located in the db folder

### Insert data in the tables

1. Exec into the docker container

2. Change the working directory to `scripts` directory

3. Run the command `python insert_data.json`

#### Choice of the database

For storing profit and loss statements of companies with multiple years' worth of data, a relational database is generally a suitable choice. 
Relational databases (SQL databases) are well-suited for handling structured data with well-defined relationships between entities, such as financial statements. 
They offer robust querying capabilities, support for complex data relationships, and transactions to ensure data integrity.

Also, the data is time-series, we will use the relational database with time-series support. Hence the choice is PostgresSQL with TimescaleDB extension.

TimescaleDB is optimized for insertion since the update event is very rare.

Comparison on TimescaleDB Vs Mongo for time-series data:
1. 260% higher insertion performance
2. 54 times Faster queries
3. Time oriented analytics functions (such as candle sticks)
4. Stable and tested Postgres database
5. Use PostgresSQl for non time-series data in the same database
