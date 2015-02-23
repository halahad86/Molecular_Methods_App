# Registers the models with the admin interface

from django.contrib import admin
from desktop.models import User, Result, Glossary, QQuestion, Answer, Lab, MQuestion, Video

#admin.site.register(User)
admin.site.register(Result)
admin.site.register(Glossary)
admin.site.register(QQuestion)
admin.site.register(Answer)
admin.site.register(Lab)
admin.site.register(MQuestion)
admin.site.register(Video)
