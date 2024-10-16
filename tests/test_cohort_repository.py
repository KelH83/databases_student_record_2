from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/student_records_2.sql") 
    repository = CohortRepository(db_connection)

    cohorts = repository.all() 

    assert cohorts == [
        Cohort(1,"Humans", 2024),
        Cohort(2,"Doggos", 2015),
        Cohort(3,'Kitties', 2012),
    ]

def test_get_all_students_in_a_cohort(db_connection):
    db_connection.seed("seeds/student_records_2.sql") 
    repository = CohortRepository(db_connection)

    all_students = repository.find_all_students(2)

    assert all_students == Cohort(2, "Doggos", 2015, [
        Student("Kimiko Dogue", 2),
        Student("Kiyomi Barker", 2)
    ])