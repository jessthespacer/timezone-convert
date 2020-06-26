from datetime import datetime
import pytz
import sys

people	  = ['Amal', 'Bibek', 'Emily/Jin/Justin/Kaitlyn/Kuunal', 'Nurayim', 'Priyanka']
timezones = ['Asia/Kuwait', 'Asia/Kathmandu', 'America/Toronto', 'Asia/Bishkek', 'PST8PDT']
localFormat = "%Y-%m-%d %H:%M:%S"

if len(sys.argv) > 1:
	name = sys.argv[1]
	dateString = '2020-06-' + sys.argv[2] + ' ' + sys.argv[3] + ':00'
	me = None

	for i, person in enumerate(people):
		if name in person.lower():
			me = i
			break
	if not me:
		raise Exception('Could not find who you were looking for')

	mytz = pytz.timezone(timezones[me])
	dateLocal = mytz.localize(datetime.strptime(dateString, '%Y-%m-%d %H:%M:%S'))
	dateUTC = dateLocal.astimezone(pytz.utc)

else:
	dateUTC = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.utc)

for i, tz in enumerate(timezones):
    localDatetime = dateUTC.astimezone(pytz.timezone(tz))
    print(people[i] + ' (' + timezones[i] + '):')
    print(localDatetime.strftime(localFormat))
    print()