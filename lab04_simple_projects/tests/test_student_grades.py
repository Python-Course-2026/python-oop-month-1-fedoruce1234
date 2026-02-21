from lab04_simple_projects.tasks.student_grades import Student

def test_student_grades():
    s = Student('A')
    s.add_grade(5)
    s.add_grade(3)
    assert s.average() == 4.0
