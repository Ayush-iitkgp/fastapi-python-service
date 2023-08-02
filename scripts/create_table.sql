CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE currency (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  currency_code VARCHAR(3) NOT NULL
);

CREATE TABLE pnl (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  currency_id UUID NOT NULL,
  data_key VARCHAR(50) NOT NULL,
  data_value NUMERIC NOT NULL,
  report_date DATE NOT NULL,
  FOREIGN KEY (currency_id) REFERENCES currency (id)
);