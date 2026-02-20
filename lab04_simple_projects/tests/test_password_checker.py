
from lab04_simple_projects.tasks.password_checker import PasswordChecker

def test_password_checker():
    assert PasswordChecker('Pass1234').is_strong() is True
