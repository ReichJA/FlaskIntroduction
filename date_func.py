import datetime
import locale

def calc_datetime_difference(date1, date2):
    diff = date2 - date1
    return diff.seconds

def date_format():

    # locale.setlocale(locale.LC_TIME,'')
    # date_format = locale.nl_langinfo(locale.D_FMT)
    date_format = '%Y-%m-%dT%H:%M'
    return date_format

    

start = datetime.datetime.strptime('2020-06-27T22:41', date_format())
print(start.year)
print(start.month)
print(start.day)

end = datetime.datetime.strptime('2020-06-27T23:41', date_format())

diff = calc_datetime_difference(start, end)

print(diff)

