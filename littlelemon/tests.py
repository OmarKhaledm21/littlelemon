from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Pizza', price=10.00, inventory=10)
        self.assertEqual(item.__str__(), "Pizza : 10.0")