

from lab03_lists_of_objects.tasks.product import Product

def test_product():
    p = Product('Apple', 2.0)
    assert p.get_total(5) == 10.0

