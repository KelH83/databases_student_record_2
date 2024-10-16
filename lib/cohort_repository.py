from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (cohort_name, starting_date) VALUES (%s, %s)', [
                                cohort.cohort_name, cohort.starting_date])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"],row["cohort_name"], row["starting_date"])
            cohorts.append(item)
        return cohorts
    
    def find_all_students(self, cohort_id):
        rows = self._connection.execute("SELECT cohorts.id AS cohort_id, cohorts.starting_date,cohorts.cohort_name, students.full_name, students.id AS student_id "  
        "FROM cohorts JOIN students ON cohorts.id = students.cohort_id "
        "WHERE cohorts.id = %s", 
        [cohort_id])

        students = []
        for row in rows:
            student = Student(row['full_name'],row["cohort_id"])
            students.append(student)

        return Cohort(rows[0]["cohort_id"],rows[0]["cohort_name"], rows[0]["starting_date"], students)
        
