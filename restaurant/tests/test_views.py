from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=100, inventory=50)

    def test_get_all(self):
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        expected_data = serializer.data
        # primer preverbe dolžine, da so res 2 elementi
        self.assertEqual(len(expected_data), 2)
