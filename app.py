from lib.database_connection import DatabaseConnection
from lib.student_repository import StudentRepository
from lib.cohort_repository import CohortRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_records_2.sql")

# # Retrieve all students
student_repository = StudentRepository(connection)
students = student_repository.all()

# # List them out
for student in students:
    print(student)

# # Retrieve all cohorts
cohort_repository = CohortRepository(connection)
cohorts = cohort_repository.all()

# # List them out
for cohort in cohorts:
    print(cohort)