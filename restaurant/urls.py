from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, index, MenuItemsView, SingleMenuItemView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name='index'),

    # Dodaj REST API za menu
    path('menu/', MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
]
