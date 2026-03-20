from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='user')
router.register('leaves', LeaveViewSet, basename='leave')
router.register('supervisors', SuperVisorViewSet, basename='supervisor')
router.register('leave-types', LeaveTypeViewSet, basename='leave-type')
router.register('leave-date-types', LeaveDateTypeViewSet, basename='leave-date-type')

urlpatterns = router.urls