from django.core.management.base import BaseCommand

import desktop.models


class Command(BaseCommand):

    args = 'No arguments'

    help = 'Populate video table of database'

    def handle(self, *args, **options):

        desktop.models.Video.objects.get_or_create(
            title="Introduction",
            link="http://youtu.be/GgcGFyDvyFA",
            topic="General")[0]

        desktop.models.Video.objects.get_or_create(
            title="PCR Primer Design",
            link="http://youtu.be/c-f1H07D_70",
            topic="Primers")[0]

        desktop.models.Video.objects.get_or_create(
            title="Restriction Mapping Part 1",
            link="http://youtu.be/yR_heZ4n4Gc",
            topic="Restriction Mapping")[0]

        desktop.models.Video.objects.get_or_create(
            title="Restriction Mapping Part 2",
            link="http://youtu.be/MeTWD8ECeiQ",
            topic="Restriction Mapping")[0]

        desktop.models.Video.objects.get_or_create(
            title="Preparing Solutions Part 1",
            link="http://youtu.be/vOwdQRBENJQ",
            topic="General")[0]

        desktop.models.Video.objects.get_or_create(
            title="Preparing Solutions Part 2",
            link="http://youtu.be/pVNpFP2Wmlc",
            topic="General")[0]

        desktop.models.Video.objects.get_or_create(
            title="Preparing Solutions Part 3",
            link="http://youtu.be/vHx4nqRdpMg",
            topic="General")[0]
