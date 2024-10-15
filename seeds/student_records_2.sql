DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS cohorts;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name VARCHAR(250),
  starting_date int
);

INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Humans', 2024);
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Doggos', 2015);
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Kitties', 2012);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(250),
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

INSERT INTO students (full_name, cohort_id) VALUES ('Kelly Howes', 1);
INSERT INTO students (full_name, cohort_id) VALUES ('Kimiko Dogue', 2);
INSERT INTO students (full_name, cohort_id) VALUES ('Kiyomi Barker', 2);
INSERT INTO students (full_name, cohort_id) VALUES ('Twyla Kitty', 3);
INSERT INTO students (full_name, cohort_id) VALUES ('Mini Panther', 3);
