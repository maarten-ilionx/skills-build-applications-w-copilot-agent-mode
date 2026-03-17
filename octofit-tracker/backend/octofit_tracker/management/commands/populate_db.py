from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Verwijder bestaande data
        get_user_model().objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Voeg teams toe
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Voeg gebruikers toe
        User = get_user_model()
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)

        # Voeg activiteiten toe
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)

        # Voeg workouts toe
        Workout.objects.create(name='Pushups', description='20 pushups')
        Workout.objects.create(name='Situps', description='30 situps')

        # Voeg leaderboard toe
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db succesvol gevuld met testdata.'))
