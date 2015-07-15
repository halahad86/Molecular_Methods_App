from django.contrib.auth.models import User
from models import MQuestion
from django import forms

# User registration form

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# Restriction mapping form

class MQuestionForm(forms.ModelForm):
    qNum = forms. ModelChoiceField(MQuestion.objects.all(), empty_label="(Nothing)")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = MQuestion
