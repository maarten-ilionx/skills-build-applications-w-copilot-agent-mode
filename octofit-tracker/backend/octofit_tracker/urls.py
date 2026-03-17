from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
	codespace_name = os.environ.get('CODESPACE_NAME')
	if codespace_name:
		base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
	else:
		base_url = request.build_absolute_uri('/api/')
	return Response({
		'users': base_url + 'users/',
		'teams': base_url + 'teams/',
		'activities': base_url + 'activities/',
		'workouts': base_url + 'workouts/',
		'leaderboard': base_url + 'leaderboard/',
	})

from django.urls import re_path
urlpatterns = [
	re_path(r'^$', api_root, name='api-root'),
	re_path(r'^api/', include(router.urls)),
]
