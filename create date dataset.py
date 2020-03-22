import random
import time
import datetime

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)
    #print(ptime)
    #return time.strptime('%m/%d/%Y', time.localtime(ptime))
    #print(datetime.datetime.fromtimestamp(ptime).date().strftime('%m-%d-%Y'))
    return datetime.datetime.fromtimestamp(ptime).date().strftime('%d-%m-%Y')


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y %I:%M %p', prop)
    #return str_time_prop(start, end, '%m/%d/%Y', prop.date())

for i in range(0, 100):
    print(random_date("1/3/2020 1:30 PM", "14/3/2020 4:50 AM", random.random()))