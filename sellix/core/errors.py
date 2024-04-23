from enum import Enum


class SellixError(Enum):
    """
    A class representing error codes returned by Sellix API.

    These errors may occur during interactions with the Sellix API.

    ---
    Reference: [sellix.errors](https://docs.sellix.io/api-reference/errors#types)
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


class CryptoGateway(Enum):
    """
    A class for representing crypto gateways.

    ---
    Reference: [sellix.paymentmethods](https://docs.sellix.io/api-reference/payment-methods#crypto)
    """

    Circle_USD = "USDC"
    """Circle USD gateway."""

    Tether_USD = "USDT"
    """Tether USD gateway."""

    Pepe = "PEPE"
    """Pepe gateway."""

    DAI = "DAI"
    """DAI gateway."""

    Wrapped_Ethereum = "WETH"
    """Wrapped Ethereum gateway."""

    Ape_Coin = "APE"
    """Ape Coin gateway."""

    Shiba_Inu = "SHIB"
    """Shiba Inu gateway."""

    Circle_USD_Native = "USDC_NATIVE"
    """Circle USD (Native) gateway."""

    Dogecoin = "DOGECOIN"
    """Dogecoin gateway."""

    Pyth = "PYTH"
    """Pyth gateway."""

    Bonk = "BONK"
    """Bonk gateway."""

    Jup = "JUP"
    """Jup gateway."""

    Jito = "JITO"
    """Jito gateway."""

    Wen = "WEN"
    """Wen gateway."""

    Render = "RENDER"
    """Render gateway."""

    Mobile = "MOBILE"
    """Mobile gateway."""

    Hnt = "HNT"
    """Hnt gateway."""


class Blockchain(Enum):
    """
    A class for representing blockchain techonologies.

    ---
    ---
    Reference: [sellix.paymentmethods](https://docs.sellix.io/api-reference/payment-methods#crypto)
    """

    ERC20 = "ERC20"
    """Ethereum blockchain."""

    BEP20 = "BEP20"
    """Binance Smart Chain blockchain."""

    MATIC = "MATIC"
    """Polygon (formerly Matic) blockchain."""

    SOL = "SOL"
    """Solana blockchain."""

    TRC20 = "TRC20"
    """TRON blockchain."""


class FiatGateway(Enum):
    PayPal = (
        "PAYPAL",
        "Use PayPal as a payment gateway and its Alternative Payment Methods (APMs)",
    )
    """PayPal gateway."""

    Stripe = "STRIPE", "Accept Credit Cards through Stripe"
    """Stripe gateway."""

    Skrill = "SKRILL", "Use your Business Skrill account"
    """Skrill gateway."""

    Perfect_Money = "PERFECT_MONEY", "Use your connected Perfect Money account"
    """Perfect Money gateway."""

    Cash_App = (
        "CASH_APP",
        "Use the Sellix Cash App integration to accept Cash App payments",
    )
    """Cash App gateway."""


class OtherGateway(Enum):
    Binance_Pay = "BINANCE", "Accept payments through Binance Pay"
    """Binance Pay gateway."""
