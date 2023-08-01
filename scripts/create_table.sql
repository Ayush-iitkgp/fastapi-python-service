CREATE TABLE currency (
  currency_id SERIAL PRIMARY KEY,
  currency_code VARCHAR(3) NOT NULL
);

CREATE TABLE pnl (
  pnl_id SERIAL PRIMARY KEY,
  currency_id INTEGER NOT NULL,
  data_key VARCHAR(50) NOT NULL,
  data_value NUMERIC NOT NULL,
  report_date DATE NOT NULL,
  FOREIGN KEY (currency_id) REFERENCES currency (currency_id)
);

-- Further improvements if companies are added
-- 1. Add company table
-- CREATE TABLE company (
-- company_id SERIAL PRIMARY KEY,
-- company_name VARCHAR(100) NOT NULL
-- );
-- 2. Add a column company id and a constraint in the pnl table
-- company_id INTEGER NOT NULL,
-- FOREIGN KEY (company_id) REFERENCES company (company_id),

-- Further optimisation if more data is added over time
-- 1. Use timescale DB extension with postgresSQL.
-- With the TimescaleDB hypertable, you can now efficiently store and query the profit
-- and loss data over time. TimescaleDB will automatically handle data partitioning, compression,
-- and indexing to optimize the performance of time-series queries, making it suitable for
-- managing large volumes of time-stamped data efficiently.
-- 2.Change report_date column to type TIMESTAMP.
-- We specify this column as the time-based dimension that will be used to partition
-- and organize the time-series data efficiently.
-- 3. Create a hypertable using TimescaleDB to optimize time-series data storage.
-- SELECT create_hypertable('pnl', 'report_date');

