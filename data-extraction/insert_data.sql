DROP TABLE IF EXISTS fact_history.fact_deaths;

CREATE TABLE fact_history.fact_deaths (
    id int NOT NULL AUTO_INCREMENT,
    dates datetime,
    country varchar(255),
    deaths int
); 

COPY 
    fact_history.fact_deaths(dates, country, deaths)
FROM 
    './deaths_data.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS fact_history.fact_confirmed;

CREATE TABLE fact_history.fact_confirmed (
    id int NOT NULL AUTO_INCREMENT,
    dates datetime,
    country varchar(255),
    confirmed int
);

COPY 
    fact_history.fact_confirmed(dates, country, confirmed)
FROM 
    './confirmed_data.csv' DELIMITER ',' CSV HEADER;