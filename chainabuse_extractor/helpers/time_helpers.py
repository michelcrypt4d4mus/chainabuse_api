import re
from typing import Union

import pendulum
from pendulum import DateTime

from chainabuse_extractor.helpers.logging_helper import log

CHAINABUSE_LAUNCH_TIME = pendulum.datetime(2008, 1, 1, tz='UTC')
MAX_TIME = DateTime.now().add(years=1)


def ms_to_datetime(ms: Union[float, int, str]) -> DateTime:
    ms = float(ms)

    try:
        datetime = pendulum.from_timestamp(float(ms))
    except ValueError as e:
        if not re.match('year \\d+ is out of range', str(e)):
            raise e

        datetime = pendulum.from_timestamp(float(ms) / 1000.0)

    log.debug(f"Extracted time {datetime} from {ms}")
    return datetime


def str_to_timestamp(iso_timestamp_string: str) -> DateTime:
    timestamp = DateTime.fromisoformat(iso_timestamp_string)

    try:
        is_valid_timestamp(timestamp)
    except TypeError as e:
        if "can't compare offset-naive and offset-aware datetimes" in str(e):
            log.warning(f"No timezone provided in '{iso_timestamp_string}'. Appending +00:00 for UTC...")
            return str_to_timestamp(iso_timestamp_string + '+00:00')

    return timestamp


def is_valid_timestamp(timestamp: DateTime) -> bool:
    if timestamp < CHAINABUSE_LAUNCH_TIME:
        raise ValueError(f"{timestamp} is before {CHAINABUSE_LAUNCH_TIME}!")
    elif timestamp > MAX_TIME:
        raise ValueError(f"{timestamp} is too far in the future!")

    return True
