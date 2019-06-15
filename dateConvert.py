import datetime
def formatDatetimeString(dateTime):
    datetime_str = dateTime
    datetime_split = datetime.datetime.strftime(datetime_str, "%Y-%m-%dT%H:%M:%S")
    return datetime_split