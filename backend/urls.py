from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'user-types', views.UserTypeViewSet)
router.register(r'users', views.UserViewSet)
