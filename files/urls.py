from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()

router.register('files',views.FileViewSet)

urlpatterns = router.urls