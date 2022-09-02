from datetime import datetime
from datetime import date
import pytz


def get_date():
    current_day = date.today()
    return current_day


def get_time():
    timezone = pytz.timezone('America/New_York')
    now = datetime.now(timezone)
    current_time = now.strftime("%I:%M:%S")
    return current_time