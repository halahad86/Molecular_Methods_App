from django.db import models
from django.contrib import admin
from app.models import Glossary, QQuestion, Answer, Lab, MQuestion, Video
from redactor.widgets import AdminRedactorEditor
# from import_export.admin import ImportExportModelAdmin
# from import_export import resources

# # Classes to override default text fields with the redactor widget
# # and to add import and export buttons for all database tables
#
# class GlossaryIE(resources.ModelResource):
#     class Meta:
#         model=Glossary
#
# class GlossaryIEButton(ImportExportModelAdmin):
#     resource_class = GlossaryIE
#     pass
#
# class QQuestionIE(resources.ModelResource):
#     class Meta:
#         model=QQuestion
#
# class QQuestionIEButton(ImportExportModelAdmin):
#     resource_class = QQuestionIE
#     formfield_overrides = {
#         models.TextField: {
#             'widget': AdminRedactorEditor
#         }
#     }
#
# class AnswerIE(resources.ModelResource):
#     class Meta:
#         model=Answer
#
# class AnswerIEButton(ImportExportModelAdmin):
#     resource_class = AnswerIE
#     formfield_overrides = {
#         models.TextField: {
#             'widget': AdminRedactorEditor
#         }
#     }
#
# class LabIE(resources.ModelResource):
#     class Meta:
#         model=Lab
#
# class LabIEButton(ImportExportModelAdmin):
#     resource_class = LabIE
#     formfield_overrides = {
#         models.TextField: {
#             'widget': AdminRedactorEditor
#         }
#     }
#
# class MQuestionIE(resources.ModelResource):
#     class Meta:
#         model=MQuestion
#
# class MQuestionIEButton(ImportExportModelAdmin):
#     resource_class = MQuestionIE
#     pass
#
# class VideoIE(resources.ModelResource):
#     class Meta:
#         model=Video
#
# class VideoIEButton(ImportExportModelAdmin):
#     resource_class = VideoIE
#     pass

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

# admin.site.register(Glossary, GlossaryIEButton)
# admin.site.register(QQuestion, QQuestionIEButton)
# admin.site.register(Answer, AnswerIEButton)
# admin.site.register(Lab, LabIEButton)
# admin.site.register(MQuestion, MQuestionIEButton)
# admin.site.register(Video, VideoIEButton)

admin.site.register(Glossary)
admin.site.register(QQuestion)
admin.site.register(Answer)
admin.site.register(Lab)
admin.site.register(MQuestion)
admin.site.register(Video)
