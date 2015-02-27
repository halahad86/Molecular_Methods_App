from django.db import models
from django.contrib import admin
from desktop.models import Glossary, QQuestion, Answer, Lab, MQuestion, Video
from redactor.widgets import AdminRedactorEditor

# Classes to override default text fields with the redactor widget

class QQuestionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': AdminRedactorEditor
        }
    }

class AnswerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': AdminRedactorEditor
        }
    }

class LabAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': AdminRedactorEditor
        }
    }

# Registration of the tables to be displayed in the admin interface, and their admin forms

admin.site.register(Glossary)
admin.site.register(QQuestion, QQuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(MQuestion)
admin.site.register(Video)
