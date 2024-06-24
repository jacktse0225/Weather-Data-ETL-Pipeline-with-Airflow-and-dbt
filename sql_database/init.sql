CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(50),
    region VARCHAR(50),
    country VARCHAR(50),
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    tz_id VARCHAR(50),
    localtime_epoch BIGINT,
    "localtime" TIMESTAMP
);
