from lib.student_repository import StudentRepository
from lib.student import Student


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/student_records_2.sql")  
    repository = StudentRepository(db_connection)

    students = repository.all() 

    assert students == [
        Student("Kelly Howes", 1),
        Student("Kimiko Dogue", 2),
        Student('Kiyomi Barker', 2),
        Student('Twyla Kitty', 3),
        Student('Mini Panther', 3),
    ]
