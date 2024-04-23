from enum import Enum


class SellixError(Enum):
    """
    A class representing error codes returned by Sellix API.

    These errors may occur during interactions with the Sellix API.

    Ref: [sellix](https://docs.sellix.io/api-reference/errors#types)
    """

    BAD_REQUEST = "Bad Request - Invalid parameters.", 400
    """
    Represents a bad request error with code 400.
    - `BAD_REQUEST`: Bad Request - Invalid parameters.
    """

    UNAUTHORIZED = "Unauthorized - Unable to authenticate.", 401
    """
    Represents an unauthorized error with code 401.
    - `UNAUTHORIZED`: Unauthorized - Unable to authenticate.
    """

    FORBIDDEN = "Forbidden - The request is not allowed.", 403
    """
    Represents a forbidden error with code 403.
    - `FORBIDDEN`: Forbidden - The request is not allowed.
    """

    NOT_FOUND = "Not Found - The specified resource could not be found.", 404
    """
    Represents a not found error with code 404.
    - `NOT_FOUND`: Not Found - The specified resource could not be found.
    """

    NOT_ACCEPTABLE = "Not Acceptable - You requested a format that isn't json.", 406
    """
    Represents a not acceptable error with code 406.
    - `NOT_ACCEPTABLE`: Not Acceptable - You requested a format that isn't json.
    """

    TOO_MANY_REQUESTS = "Too Many Requests - You have reached the rate limit.", 429
    """
    Represents a too many requests error with code 429.
    - `TOO_MANY_REQUESTS`: Too Many Requests - You have reached the rate limit.
    """

    INTERNAL_SERVER_ERROR = (
        "Internal Server Error - We had a problem with our server. Try again later. These are rare.",
        500,
    )
    """
    Represents an internal server error with code 500.
    - `INTERNAL_SERVER_ERROR`: Internal Server Error - We had a problem with our server. Try again later. These are rare.
    """

    SERVICE_UNAVAILABLE = (
        "Service Unavailable - We're temporarily offline for maintenance. Please try again later.",
        503,
    )
    """
    Represents a service unavailable error with code 503.
    - `SERVICE_UNAVAILABLE`: Service Unavailable - We're temporarily offline for maintenance. Please try again later.
    """

    RATE_LIMIT_EXCEEDED = (
        "Rate-limiting errors (429) happen when you are sending too many requests to the developers API.",
        429,
    )
    """
    Represents a rate limit exceeded error with code 429.
    - `RATE_LIMIT_EXCEEDED`: Rate-limiting errors (429) happen when you are sending too many requests to the developers API.
    """
