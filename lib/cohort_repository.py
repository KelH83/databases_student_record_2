from lib.cohort import Cohort

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
            item = Cohort(row["cohort_name"], row["starting_date"])
            cohorts.append(item)
        return cohorts