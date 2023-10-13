from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
