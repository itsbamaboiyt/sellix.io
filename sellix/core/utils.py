import typing as t


def if_int(value: t.Any) -> bool:
    """
    Checks if the input value is an integer.

    Args:
    value: The value to check.

    Returns:
    bool: True if the value is an integer, False otherwise.
    """

    return isinstance(value, int)


def if_bool(value: t.Any) -> t.Optional[bool]:
    """
    Checks if the input value is a boolean representation.

    Args:
        value: The value to check.

    Returns:
        Optional[bool]: True if the value is "true", False if the value is "false", None otherwise.
    """

    if value == "false":
        return False
    elif value == "true":
        return True
    else:
        return None
