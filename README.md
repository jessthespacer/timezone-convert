# timezone-convert
To use, run the code from the command line. All times use **24-hour** format.

This code requires the `pytz` module to be installed. If you do not have it, run `pip install pytz` from the command line.

# Get times for everyone right now
To get times for everyone right now, run `py timezone-convert.py`.
Example output:
<pre><code>Right now, it is:

Amal (Asia/Kuwait):
2020-06-26 21:08:15

Bibek (Asia/Kathmandu):
2020-06-26 23:53:15

Emily/Jin/Justin/Kaitlyn/Kuunal (America/Toronto):
2020-06-26 14:08:15

Nuraiym (Asia/Bishkek):
2020-06-27 00:08:15

Priyanka (PST8PDT):
2020-06-26 11:08:15
</code></pre>

# Convert one person's timezone to another's
To convert one person's timezone to another, run `py timezone-convert.py [name] [month-day] [time]`
This will convert `[time]` on `[month-day]` in `[name]`'s timezone to everyone else's.

For example, `py timezone-convert.py jin 06-26 20:00` will print:
<pre><code>At 2020-06-26 20:00:00 in Emily/Jin/Justin/Kaitlyn/Kuunal's timezone, it is:

Amal (Asia/Kuwait):
2020-06-27 03:00:00

Bibek (Asia/Kathmandu):
2020-06-27 05:45:00

Emily/Jin/Justin/Kaitlyn/Kuunal (America/Toronto):
2020-06-26 20:00:00

Nuraiym (Asia/Bishkek):
2020-06-27 06:00:00

Priyanka (PST8PDT):
2020-06-26 17:00:00
</code></pre>
