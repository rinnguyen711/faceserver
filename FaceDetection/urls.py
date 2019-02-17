from .views import FaceDetectionViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('faces',viewset=FaceDetectionViewSet, base_name='faces')

urlpatterns = router.urls