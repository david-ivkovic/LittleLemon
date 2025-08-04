from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Cake", Price=100, Inventory=50)

    def test_get_all(self):
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        expected_data = serializer.data
        # primer preverbe dolžine, da so res 2 elementi
        self.assertEqual(len(expected_data), 2)
