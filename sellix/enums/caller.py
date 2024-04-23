from enum import Enum


class Currency(Enum):
    """
    Class that represents a currecny.

    ---
    Reference: [sellix.get_self](https://docs.sellix.io/api-reference/information/get-self)
    """

    CAD = "Canadian Dollar"
    """Represents the Canadian Currency `dollar` 🇨🇦"""

    HKD = "Hong Kong Dollar"
    """Represents the Hong Kong Currency `dollar` 🇭🇰"""

    ISK = "Icelandic Króna"
    """Represents the Icelandic Currency `króna` 🇮🇸"""

    PHP = "Philippine Peso"
    """Represents the Philippine Currency `peso` 🇵🇭"""

    DKK = "Danish Krone"
    """Represents the Danish Currency `krone` 🇩🇰"""

    HUF = "Hungarian Forint"
    """Represents the Hungarian Currency `forint` 🇭🇺"""

    CZK = "Czech Koruna"
    """Represents the Czech Currency `koruna` 🇨🇿"""

    GBP = "British Pound Sterling"
    """Represents the British Currency `pound sterling` 🇬🇧"""

    RON = "Romanian Leu"
    """Represents the Romanian Currency `leu` 🇷🇴"""

    SEK = "Swedish Krona"
    """Represents the Swedish Currency `krona` 🇸🇪"""

    IDR = "Indonesian Rupiah"
    """Represents the Indonesian Currency `rupiah` 🇮🇩"""

    INR = "Indian Rupee"
    """Represents the Indian Currency `rupee` 🇮🇳"""

    BRL = "Brazilian Real"
    """Represents the Brazilian Currency `real` 🇧🇷"""

    RUB = "Russian Ruble"
    """Represents the Russian Currency `ruble` 🇷🇺"""

    HRK = "Croatian Kuna"
    """Represents the Croatian Currency `kuna` 🇭🇷"""

    JPY = "Japanese Yen"
    """Represents the Japanese Currency `yen` 🇯🇵"""

    THB = "Thai Baht"
    """Represents the Thai Currency `baht` 🇹🇭"""

    CHF = "Swiss Franc"
    """Represents the Swiss Currency `franc` 🇨🇭"""

    EUR = "Euro"
    """Represents the European Currency `euro` 🇪🇺"""

    MYR = "Malaysian Ringgit"
    """Represents the Malaysian Currency `ringgit` 🇲🇾"""

    BGN = "Bulgarian Lev"
    """Represents the Bulgarian Currency `lev` 🇧🇬"""

    TRY = "Turkish Lira"
    """Represents the Turkish Currency `lira` 🇹🇷"""

    CNY = "Chinese Yuan"
    """Represents the Chinese Currency `yuan` 🇨🇳"""

    NOK = "Norwegian Krone"
    """Represents the Norwegian Currency `krone` 🇳🇴"""

    NZD = "New Zealand Dollar"
    """Represents the New Zealand Currency `dollar` 🇳🇿"""

    ZAR = "South African Rand"
    """Represents the South African Currency `rand` 🇿🇦"""

    USD = "United States Dollar"
    """Represents the United States Currency `dollar` 🇺🇸"""

    MXN = "Mexican Peso"
    """Represents the Mexican Currency `peso` 🇲🇽"""

    SGD = "Singapore Dollar"
    """Represents the Singapore Currency `dollar` 🇸🇬"""

    AUD = "Australian Dollar"
    """Represents the Australian Currency `dollar` 🇦🇺"""

    ILS = "Israeli New Shekel"
    """Represents the Israeli Currency `new shekel` 🇮🇱"""

    KRW = "South Korean Won"
    """Represents the South Korean Currency `won` 🇰🇷"""

    PLN = "Polish Zloty"
    """Represents the Polish Currency `zloty` 🇵🇱"""


class DashboardFeature(Enum):
    API_CUSTOM = "API_CUSTOM"
    """Represents the organization mode set for the dashboard as API Custom."""

    EMBED = "EMBED"
    """Represents the organization mode set for the dashboard as Embed."""

    PAYMENT_LINKS = "PAYMENT_LINKS"
    """Represents the organization mode set for the dashboard as Payment Links."""

    STORE = "STORE"
    """Represents the organization mode set for the dashboard as Store."""

    POS = "POS"
    """Represents the organization mode set for the dashboard as Point of Sale (POS)."""

    PLUGINS = "PLUGINS"
    """Represents the organization mode set for the dashboard as Plugins."""

    UNSURE = "UNSURE"
    """Represents an unsure state for the organization mode set for the dashboard."""


class SortCustomTheme(Enum):
    DEFAULT = "DEFAULT"
    """Default sorting method for the storefront's custom theme."""

    PRICE = "PRICE"
    """Sort by price for the storefront's custom theme."""

    STOCK = "STOCK"
    """Sort by stock for the storefront's custom theme."""

    NAME = "NAME"
    """Sort by name for the storefront's custom theme."""

    TYPE = "TYPE"
    """Sort by type for the storefront's custom theme."""


class DefaultSort(Enum):
    DEFAULT = "DEFAULT"
    """Default sorting method for the storefront."""

    PRICE = "PRICE"
    """Sort by price for the storefront."""

    STOCK = "STOCK"
    """Sort by stock for the storefront."""

    NAME = "NAME"
    """Sort by name for the storefront."""

    TYPE = "TYPE"
    """Sort by type for the storefront."""


class SetupWizard(Enum):
    NOT_COMPLETED = 0
    """The shop has not completed the setup wizard."""

    COMPLETED = 1
    """The shop has completed the setup wizard."""


class SetupCryptocurrencies(Enum):
    NOT_SETUP = 0
    """Cryptocurrencies have not been set up for the shop."""

    SETUP = 1
    """Cryptocurrencies have been set up for the shop."""
