from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, index, MenuItemsView, SingleMenuItemView, msg
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('message/', msg, name='protected-message'),  # <-- dodaj to vrstico!
    path('api-token-auth/', obtain_auth_token),
]
