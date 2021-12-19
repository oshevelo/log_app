import uuid


def parse_int(value):
    """ Return the value casted to integer, or None if casting is not possible.
    """
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def parse_bool(value):
    return value in [1, "1", 'true', 't', 'True']


def parse_uuid(value):
    """ Return the value casted to UUID, or NOne if casting is not possible
    """
    try:
        return uuid.UUID(value)
    except (TypeError, ValueError):
        return None


def float_or_as_is(value):
    """ Return value casted to float or the original value, if the cast is impossible
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        return value
