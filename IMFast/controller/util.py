from datetime import datetime
from pytz import utc


def utc_now() -> datetime:
    return datetime.now(utc)
