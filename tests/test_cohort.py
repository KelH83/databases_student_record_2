from lib.cohort import Cohort

def test_student_constructs():
    cohort = Cohort("Snakes", 2010)
    assert cohort.cohort_name == "Snakes"
    assert cohort.starting_date == 2010

def test_students_format_nicely():
    cohort = Cohort("Snakes", 2010)
    assert str(cohort) == "Cohort Name:Snakes,Starting date:2010"