from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='TestTeam')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test', team=self.team)
        self.workout = Workout.objects.create(name='TestWorkout', description='desc')
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_users_list(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_list(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activities_list(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, 200)

    def test_workouts_list(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
