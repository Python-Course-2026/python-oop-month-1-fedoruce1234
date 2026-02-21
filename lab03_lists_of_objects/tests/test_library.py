

from lab03_lists_of_objects.tasks.library import Library

def test_library():
    lib = Library()
    lib.add_book('Python Basics')
    assert len(lib.books) == 1

