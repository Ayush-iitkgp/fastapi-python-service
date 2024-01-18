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