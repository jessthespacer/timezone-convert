from datetime import datetime
import pytz
import sys

people	  = ['Amal', 'Bibek', 'Emily/Jin/Justin/Kaitlyn/Kuunal', 'Nuraiym', 'Priyanka', 'CEST']
timezones = ['Asia/Kuwait', 'Asia/Kathmandu', 'America/Toronto', 'Asia/Bishkek', 'PST8PDT', 'Europe/Berlin']
localFormat = "%Y-%m-%d %H:%M:%S"

if len(sys.argv) > 1:
	name = sys.argv[1]
	dateString = '2020-' + sys.argv[2] + ' ' + sys.argv[3] + ':00'
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

	print('At ', dateString, ' in ', people[me], '\'s timezone, it is:', sep='')
	print()
else:
	dateUTC = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.utc)
	print('Right now, it is:')
	print()

for i, tz in enumerate(timezones):
    localDatetime = dateUTC.astimezone(pytz.timezone(tz))
    print(people[i] + ' (' + timezones[i] + '):')
    print(localDatetime.strftime(localFormat))
    print()