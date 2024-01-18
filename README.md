### Prerequisites

Project requires python 3.10.8, pyenv, colima, docker, and poetry.

Install `pyenv` tool to manage python version.

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
3. Change the working directory to `scripts` directory
```bash
cd scripts
```
4. Run the python command 
```bash
python insert_data.py
```

### Testing

`pytest` will run all unit tests that you specify in your codebase.

As pytest convention, all files matching `test_*.py` will be included.

#### Running tests
```bash
docker-compose run app bash
poetry run pytest
```

#### Possible future improvements
- Implement Authentication - **DONE**
- Write (more) tests and fix the not working test
- Implement CI/CD Pipeline
- Github hooks for formatting the code
