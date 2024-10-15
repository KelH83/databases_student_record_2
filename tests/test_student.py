from lib.student import Student

def test_student_constructs():
    student = Student("Kyoko Howes", 1)
    assert student.full_name == "Kyoko Howes"
    assert student.cohort_id == 1

def test_students_format_nicely():
    student = Student("Kyoko Howes", 1)
    assert str(student) == "Name:Kyoko Howes,Cohort ID:1"