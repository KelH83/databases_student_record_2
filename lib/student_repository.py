from lib.student import Student

class StudentRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from students')
        students = []
        for row in rows:
            item = Student(row["full_name"], row["cohort_id"])
            students.append(item)
        return students

    