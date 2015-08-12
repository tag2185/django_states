#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_states.settings")

from main.models import State, StateCapital

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.csv")

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

print reader

for row in reader:
	state_obj, created = State.objects.get_or_create(name=row['state'])
	#state_obj.name = row['state']
	state_obj.abbreviation = row['abbrev']
	state_obj.save()

	capital_obj, created = StateCapital.objects.get_or_create(name=row['capital'])
	capital_obj.latitude = row['latitude']
	capital_obj.longitude = row['longitude']
	capital_obj.population = row['population']
	capital_obj.state = state_obj

	capital_obj.save()

	# print "state:%s Abbreviation:%s Capiital:%s" % (row['state'], row['abbrev'], row['capital'])
	# print """
	# 		<h3>Welcome to {0},</h3>

	# 		<p>"State:{1} Abbreviation:{0} Capiital:{2}".format(row['state'], row['abbrev'], row['capital'])