import datetime
import locale

def calc_datetime_difference(date1, date2):
    diff = date2 - date1
    return diff.seconds/3600

def date_format():

    # locale.setlocale(locale.LC_TIME,'')
    # date_format = locale.nl_langinfo(locale.D_FMT)
    date_format = '%Y-%m-%dT%H:%M'
    return date_format

def date_to_string(date):

    if date.month < 10:
        month_as_str = f"0{date.month}"
    else:
        month_as_str = f"{date.month}"

    if date.day < 10:
        day_as_str = f"0{date.day}"
    else:
        day_as_str = f"{date.day}"

    if date.hour < 10:
        hour_as_str = f"0{date.hour}"
    else:
        hour_as_str = f"{date.hour}"

    if date.minute < 10:
        min_as_str = f"0{date.minute}"
    else:
        min_as_str = f"{date.minute}"
    
    date_as_str = f"{date.year}-{month_as_str}-{day_as_str}"
    time_as_str = f"{hour_as_str}:{min_as_str}"
    return (date_as_str, time_as_str)

start = datetime.datetime.strptime('2020-06-27T08:00', date_format())
end = datetime.datetime.strptime('2020-06-27T15:48', date_format())

diff = calc_datetime_difference(start, end)

print(diff)

