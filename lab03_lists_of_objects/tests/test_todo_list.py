
from lab03_lists_of_objects.tasks.todo_list import TodoList

def test_todo_list():
    l = TodoList()
    l.add_task('Code')
    assert 'Code' in l.tasks
