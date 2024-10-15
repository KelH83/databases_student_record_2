class Cohort:
    def __init__(self, cohort_name, starting_date):
        self.cohort_name = cohort_name
        self.starting_date = starting_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Cohort Name:{self.cohort_name},Starting date:{self.starting_date}"
