import xml.etree.ElementTree

from django.core.management.base import BaseCommand

import app.models


class Command(BaseCommand):

    args = 'No arguments'

    help = 'Populate glossary table of database'

    def handle(self, *args, **options):

        tree = xml.etree.ElementTree.parse('static/xml/Glossary.xml')

        root = tree.getroot()

        for entry in root[0][13]:
            app.models.Glossary.objects.get_or_create(title=entry[0].text, description=entry[1].text)[0]