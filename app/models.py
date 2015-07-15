from django.db import models
from django.contrib.auth.models import User
from mapping import findAns
from HTMLParser import HTMLParser

# Code for displaying the names of questions and answers without HTML tags

class HTMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = HTMLStripper()
    s.feed(html)
    return s.get_data()

class MQuestion(models.Model):
    number = models.IntegerField(primary_key=True)
    size = models.IntegerField(help_text ="All numbers give should be round numbers e.g 35 instead of 3.5 or 60 instead of 6.0")
    enzyme1 = models.CharField(max_length=200,help_text ="Please enter Enzymes such that they are of the form Name:size of the slice:size of the slice  e.g Exoir:20:50")
    enzyme2 = models.CharField(max_length=200, help_text ="Note the colons between section in the Enzyme e.g Xoire:70")
    enzyme3 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, editable = False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.answer

    def save(self, *args, **kwargs):
        ans = findAns(self.size,self.enzyme1,self.enzyme2,self.enzyme3)
        if ans == "NoSol":
            return
        else:
            self.answer = ans
            super(MQuestion, self).save(*args, **kwargs) # Call the "real" save() method.

    class Meta:
        verbose_name="a new restriction mapping question"
        verbose_name_plural = "Restriction Mapping Questions"


class QQuestion(models.Model):

    #Needed in order to have Static - hard coded question choices
    TOPICS_CHOICES = (
        (1, 'General'),
        (2, 'PCR & Primer'),
        (3, 'Restriction Mapping'),
        (4, 'Data Calculations'),
    )
    number = models.AutoField(primary_key=True)
    topic = models.IntegerField(choices=TOPICS_CHOICES, default=1)
    question = models.TextField()

    def __unicode__(self):
        return strip_tags(self.question)

    class Meta:
        verbose_name="quiz question"
        verbose_name_plural = "Quiz Questions"


class Answer(models.Model):
    number = models.AutoField(primary_key=True)
    question = models.ForeignKey('QQuestion')
    answer = models.TextField()
    correct = models.BooleanField(default=False)

    def __unicode__(self):
        return strip_tags(self.answer)

    class Meta:
        verbose_name="quiz answer"
        verbose_name_plural = "Quiz Answers"


class Video(models.Model):
    title = models.CharField(max_length=128, unique=True)
    link = models.URLField(max_length=256)
    topic = models.CharField(max_length=128)

    def __unicode__(self):
        return self.link

    class Meta:
        verbose_name="video"
        verbose_name_plural = "Videos"


class Glossary(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name="glossary term"
        verbose_name_plural = "Glossary"


class Lab(models.Model):
    name = models.CharField(max_length=256)
    number = models.IntegerField(unique=True)
    ILO = models.TextField()
    tasks = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name="lab session"
        verbose_name_plural = "Labs"

