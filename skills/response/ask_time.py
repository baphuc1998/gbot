from datetime import datetime, timedelta
from pytz import timezone
import calendar

def get_time():
    fmt = '%H:%M:%S'
    aus = timezone('Australia/Sydney')
    td = datetime.today()
    aus_dt = td.astimezone(aus)
    return aus_dt.strftime(fmt)

# print(get_time('%m-%d-%Y'))

def get_date():
    aus = timezone('Australia/Sydney')
    td = datetime.today()
    aus_dt = td.astimezone(aus)
    arr = ['Jan','Feb','Mar','Apr','May','Jun',
        'July','Aug','Sep','Oct','Nov','Dec']
    str_date = calendar.day_name[aus_dt.weekday()]+' '+str(aus_dt.day)+'-'+arr[aus_dt.month]+'-'+str(aus_dt.year)
    return str_date

print(get_time())