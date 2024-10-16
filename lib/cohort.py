class Cohort:
    def __init__(self, id, cohort_name, starting_date, students = []):
        self.id = id
        self.cohort_name = cohort_name
        self.starting_date = starting_date
        self.students = students

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Id:{self.id},Cohort Name:{self.cohort_name},Starting date:{self.starting_date}"
