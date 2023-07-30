## Set up the project

The project uses Python version 3.10.8 or above

Install tool to manage python version `pyenv`

`pyenv install 3.10.8`

Have the docker running on the local machine

`colima start`

Install Poetry 

Using poetry version 1.1.11

`pip install poetry`

Install project dependency

`poetry install`

#### Choice of the database

For storing profit and loss statements of companies with multiple years' worth of data, a relational database is generally a suitable choice. 
Relational databases (SQL databases) are well-suited for handling structured data with well-defined relationships between entities, such as financial statements. 
They offer robust querying capabilities, support for complex data relationships, and transactions to ensure data integrity.

Also, the data is time-series, we will use the relational database with time-series support. Hence the choice is PostgresSQL with TimescaleDB extension.