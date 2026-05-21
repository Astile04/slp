from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = router.urls + [
    path('auth/register/', views.RegisterView.as_view()),
]