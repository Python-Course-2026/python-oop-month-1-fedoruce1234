from lab01_intro_classes.tasks.book import Book

def test_book():
    b = Book('1984', 'Orwell')
    assert b.title == '1984'


