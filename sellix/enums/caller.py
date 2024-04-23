from enum import (
    Enum,
)


class Currency(
    Enum
):
    CANADIAN_DOLLAR = "CAD"
    """Represents the Canadian Currency `dollar` 🇨🇦"""

    HONG_KONG_DOLLAR = "HKD"
    """Represents the Hong Kong Currency `dollar` 🇭🇰"""

    ICELANDIC_KRONA = "ISK"
    """Represents the Icelandic Currency `króna` 🇮🇸"""

    PHILIPPINE_PESO = "PHP"
    """Represents the Philippine Currency `peso` 🇵🇭"""

    DANISH_KRONE = "DKK"
    """Represents the Danish Currency `krone` 🇩🇰"""

    HUNGARIAN_FORINT = "HUF"
    """Represents the Hungarian Currency `forint` 🇭🇺"""

    CZECH_KORUNA = "CZK"
    """Represents the Czech Currency `koruna` 🇨🇿"""

    BRITISH_POUND_STERLING = "GBP"
    """Represents the British Currency `pound sterling` 🇬🇧"""

    ROMANIAN_LEU = "RON"
    """Represents the Romanian Currency `leu` 🇷🇴"""

    SWEDISH_KRONA = "SEK"
    """Represents the Swedish Currency `krona` 🇸🇪"""

    INDONESIAN_RUPIAH = "IDR"
    """Represents the Indonesian Currency `rupiah` 🇮🇩"""

    INDIAN_RUPEE = "INR"
    """Represents the Indian Currency `rupee` 🇮🇳"""

    BRAZILIAN_REAL = "BRL"
    """Represents the Brazilian Currency `real` 🇧🇷"""

    RUSSIAN_RUBLE = "RUB"
    """Represents the Russian Currency `ruble` 🇷🇺"""

    CROATIAN_KUNA = "HRK"
    """Represents the Croatian Currency `kuna` 🇭🇷"""

    JAPANESE_YEN = "JPY"
    """Represents the Japanese Currency `yen` 🇯🇵"""

    THAI_BAHT = "THB"
    """Represents the Thai Currency `baht` 🇹🇭"""

    SWISS_FRANC = "CHF"
    """Represents the Swiss Currency `franc` 🇨🇭"""

    EURO = "EUR"
    """Represents the European Currency `euro` 🇪🇺"""

    MALAYSIAN_RINGGIT = "MYR"
    """Represents the Malaysian Currency `ringgit` 🇲🇾"""

    BULGARIAN_LEV = "BGN"
    """Represents the Bulgarian Currency `lev` 🇧🇬"""

    TURKISH_LIRA = "TRY"
    """Represents the Turkish Currency `lira` 🇹🇷"""

    CHINESE_YUAN = "CNY"
    """Represents the Chinese Currency `yuan` 🇨🇳"""

    NORWEGIAN_KRONE = "NOK"
    """Represents the Norwegian Currency `krone` 🇳🇴"""

    NEW_ZEALAND_DOLLAR = "NZD"
    """Represents the New Zealand Currency `dollar` 🇳🇿"""

    SOUTH_AFRICAN_RAND = "ZAR"
    """Represents the South African Currency `rand` 🇿🇦"""

    UNITED_STATES_DOLLAR = "USD"
    """Represents the United States Currency `dollar` 🇺🇸"""

    MEXICAN_PESO = "MXN"
    """Represents the Mexican Currency `peso` 🇲🇽"""

    SINGAPORE_DOLLAR = "SGD"
    """Represents the Singapore Currency `dollar` 🇸🇬"""

    AUSTRALIAN_DOLLAR = "AUD"
    """Represents the Australian Currency `dollar` 🇦🇺"""

    ISRAELI_NEW_SHEKEL = "ILS"
    """Represents the Israeli Currency `new shekel` 🇮🇱"""

    SOUTH_KOREAN_WON = "KRW"
    """Represents the South Korean Currency `won` 🇰🇷"""

    POLISH_ZLOTY = "PLN"
    """Represents the Polish Currency `zloty` 🇵🇱"""


class DashboardFeature(
    Enum
):
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


class SortCustomTheme(
    Enum
):
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


class DefaultSort(
    Enum
):
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


class SetupWizard(
    Enum
):
    NOT_COMPLETED = 0
    """The shop has not completed the setup wizard."""

    COMPLETED = 1
    """The shop has completed the setup wizard."""


class SetupCryptocurrencies(
    Enum
):
    NOT_SETUP = 0
    """Cryptocurrencies have not been set up for the shop."""

    SETUP = 1
    """Cryptocurrencies have been set up for the shop."""


class MarketplaceVerified(
    Enum
):
    NOT_VERIFIED = 0
    """The shop is not a verified marketplace."""

    VERIFIED = 1
    """The shop is a verified marketplace."""


class ShopType(
    Enum
):
    DEFAULT = "DEFAULT"
