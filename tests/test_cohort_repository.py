from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/student_records_2.sql") 
    repository = CohortRepository(db_connection)

    cohorts = repository.all() 

    assert cohorts == [
        Cohort("Humans", 2024),
        Cohort("Doggos", 2015),
        Cohort('Kitties', 2012),
    ]