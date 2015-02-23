from django.core.management.base import BaseCommand
import desktop.models

class Command(BaseCommand):

    args = 'No arguments'

    help = 'Populate restriction mapping table of database'

    def handle(self, *args, **options):

        desktop.models.MQuestion.objects.get_or_create(
            number=1,
            size=70,
            enzyme1="EcoRI:70",
            enzyme2="XhoI:55:15",
            enzyme3="EcoRI+XhoI:30:25:15")[0]

        desktop.models.MQuestion.objects.get_or_create(
            number=2,
            size=60,
            enzyme1="EcoRI:10:20:30",
            enzyme2="XhoI:60",
            enzyme3="EcoRI+XhoI:10:12:18:20")[0]

        desktop.models.MQuestion.objects.get_or_create(
            number=3,
            size=70,
            enzyme1="EcoRI:70",
            enzyme2="XhoI:60:10",
            enzyme3="EcoRI+XhoI:30:10")[0]

        desktop.models.MQuestion.objects.get_or_create(
            number=4,
            size=70,
            enzyme1="EcoRI:50:20",
            enzyme2="XhoI:60:10",
            enzyme3="EcoRI+XhoI:30:20:10")[0]

        desktop.models.MQuestion.objects.get_or_create(
            number=5,
            size=60,
            enzyme1="EcoRI:28:32",
            enzyme2="XhoI:13:47",
            enzyme3="EcoRI+XhoI:6:7:21:26")[0]

        desktop.models.MQuestion.objects.get_or_create(
            number=6,
            size=70,
            enzyme1="EcoRI:50:12:8",
            enzyme2="XhoI:40:30",
            enzyme3="EcoRI+XhoI:30:20:10:2:8")[0]
