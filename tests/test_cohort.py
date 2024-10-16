from lib.cohort import Cohort

def test_cohort_constructs():
    cohort = Cohort(1,"Snakes", 2010)
    assert cohort.cohort_name == "Snakes"
    assert cohort.starting_date == 2010

def test_cohort_format_nicely():
    cohort = Cohort(1,"Snakes", 2010)
    assert str(cohort) == "Id:1,Cohort Name:Snakes,Starting date:2010"