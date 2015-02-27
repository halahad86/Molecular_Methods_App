import os
import sys

PYTHONPATH = '/home/molecmeth/Molecular_Methods_App'

path = '/home/1102445f/www'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Molecular_Methods_Project.settings'

from django.contrib.auth.handlers.modwsgi import check_password

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

