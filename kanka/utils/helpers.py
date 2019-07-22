from datetime import datetime as _datetime
import pytz as _pytz


def time_converter(time_dict):
    """
    This function expects a dictionary with a "date" key, where the value is a string, written like this:
    2017-10-27 13:36:19.0. It also needs a "timezone" key, with a timezone as value.
    """
    time = time_dict["date"].split(".")[0]
    tz = _pytz.timezone(time_dict["timezone"])
    # function taken from https://stackoverflow.com/a/1358161
    return tz.normalize(tz.localize(_datetime.strptime(time, "%Y-%m-%d %H:%M:%S")).astimezone(_pytz.utc))
