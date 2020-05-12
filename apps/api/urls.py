from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet, WorkoutDetailsView

router = DefaultRouter()
router.register('workouts', WorkoutViewSet, basename='workouts')

custom_urlpatterns = [
    url(r'^workouts/(?P<pk>\d+)/$', WorkoutDetailsView.as_view(), name='workouts')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns