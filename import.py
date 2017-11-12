import csv, sys, os

project_dir = "/Users/priyam/Desktop/django/old_projects/beta/beta/beta"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from newspapers.models import Newspapers

data = csv.reader(open("/Users/priyam/Desktop/django/old_projects/beta/beta/newspaper_data.csv"),delimiter=",")

for row in data:
	instance = Newspapers()
	instance.title=row[0]
	instance.language=row[1]
	instance.price=row[2]
	instance.save()