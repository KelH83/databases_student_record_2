DROP TABLE IF EXISTS cohorts;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name VARCHAR(250),
  starting_date int
);

INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Humans', 2024);
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Doggos', 2015);
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Kitties', 2012);