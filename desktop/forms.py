from django import forms
from django.contrib.auth import authenticate
from desktop.models import User
from django.contrib.auth.models import User
from models import MQuestion
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class QuestionForm(forms.ModelForm):
    qNum = forms. ModelChoiceField(MQuestion.objects.all(), empty_label="(Nothing)")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = MQuestion


