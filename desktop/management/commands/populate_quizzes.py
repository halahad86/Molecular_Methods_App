import xml.etree.ElementTree

from django.core.management.base import BaseCommand

import desktop.models


class Command(BaseCommand):

    args = 'No arguments'
    help = 'Populate question and answer table of database'

    def populate(self, filename, name):

        tree = xml.etree.ElementTree.parse(filename)

        root = tree.getroot()

        questionNumber = 0

        for question in root:
            for info in question:
                if info.tag == "questiontext":
                    for question in info:
                        if question.tag == "text":
                            questionText = question.text
                            questionObject = desktop.models.QQuestion.objects.get_or_create(
                                topic=name,
                                question=questionText)[0]

                if info.tag == "answer":
                    for answer in info:
                        isCorrect = False
                        if answer.tag == "text":
                            answerText = answer.text
                            if info.attrib['fraction'] != "0":
                                isCorrect = True
                            desktop.models.Answer.objects.get_or_create(
                                question=questionObject,
                                answer=answerText,
                                correct=isCorrect)[0]

            questionNumber += 1

    def handle(self, *args, **options):
        self.populate('xml files/General.xml', 1)
        self.populate('xml files/PrimerDesign.xml', 2)
        self.populate('xml files/RestrictionMapping.xml', 3)
        self.populate('xml files/DataCalculations.xml', 4)
