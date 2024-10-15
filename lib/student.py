class Student:
    def __init__(self, full_name, cohort_id):
        self.full_name = full_name
        self.cohort_id = cohort_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Name:{self.full_name},Cohort ID:{self.cohort_id}"
