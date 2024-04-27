from enum import (
    Enum,
)


class Currency(Enum):
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


class ShopType(Enum):
    DEFAULT = "DEFAULT"
    
    
class OrderType(Enum):
    """
    Enum representing the invoice type for orders.

    For subscriptions, the invoice type is PRODUCT_SUBSCRIPTION as SUBSCRIPTION is reserved for Sellix-own plans.
    """

    PRODUCT = "PRODUCT"
    """
    Represents an invoice type for a product.
    """

    SUBSCRIPTION = "SUBSCRIPTION"
    """
    Represents an invoice type for a subscription. (Reserved for Sellix-own plans)
    """

    PUBLIC_REST_API = "PUBLIC_REST_API"
    """
    Represents an invoice type for a public REST API.
    """

    MONTHLY_BILL = "MONTHLY_BILL"
    """
    Represents an invoice type for a monthly bill.
    """

    SHOPPING_CART = "SHOPPING_CART"
    """
    Represents an invoice type for a shopping cart.
    """

    PRODUCT_SUBSCRIPTION = "PRODUCT_SUBSCRIPTION"
    """
    Represents an invoice type for a product subscription.
    """


class OrderSubtype(Enum):
    """
    Enum representing the product type for orders.
    """

    SERIALS = "SERIALS"
    """
    Represents a product subtype for serials.
    """

    FILE = "FILE"
    """
    Represents a product subtype for files.
    """

    SERVICE = "SERVICE"
    """
    Represents a product subtype for services.
    """

    DYNAMIC = "DYNAMIC"
    """
    Represents a product subtype for dynamic products.
    """

    INFO_CARD = "INFO_CARD"
    """
    Represents a product subtype for information cards.
    """

    SUBSCRIPTION = "SUBSCRIPTION"
    """
    Represents a product subtype for subscriptions.
    """
    
class OrderOrigin(Enum):
    """
    Enum representing how the invoice was created.
    """

    STOREFRONT = "STOREFRONT"
    """
    Represents an invoice created through the storefront.
    """

    API = "API"
    """
    Represents an invoice created through the API.
    """

class ProductType(Enum):
    """
    Enum representing the product type for orders.
    """

    SERIALS = "SERIALS"
    """
    Represents a product type for serials.
    """

    FILE = "FILE"
    """
    Represents a product type for files.
    """

    SERVICE = "SERVICE"
    """
    Represents a product type for services.
    """

    DYNAMIC = "DYNAMIC"
    """
    Represents a product type for dynamic products.
    """

    INFO_CARD = "INFO_CARD"
    """
    Represents a product type for information cards.
    """

    SUBSCRIPTION = "SUBSCRIPTION"
    """
    Represents a product type for subscriptions.
    """
class Gateway(Enum):
    """
    Enum representing the gateway for orders.
    """

    PAYPAL = "PAYPAL"
    """
    Represents a gateway for paypal.
    """

    STRIPE = "STRIPE"
    """
    Represents a gateway for stripe.
    """

    SKRILL = "SKRILL"
    """
    Represents a gateway for SKRILL.
    """

    PERFECT_MONEY = "PERFECT_MONEY"
    """
    Represents a gateway for Perfect Money.
    """

    CASH_APP = "CASH_APP"
    """
    Represents a gateway for Cash App.
    """

    BINANCE = "BINANCE"
    """
    Represents a gateway for Binance.
    """

    BITCOIN = "BITCOIN"
    """
    Represents a gateway for Bitcoin.
    """

    LITECOIN = "LITECOIN"
    """
    Represents a gateway for Litecoin.
    """

    ETHEREUM = "ETHEREUM"
    """
    Represents a gateway for Ethereum.
    """

    BITCOIN_CASH = "BITCOIN_CASH"
    """
    Represents a gateway for Bitcoin Cash.
    """

    NANO = "NANO"
    """
    Represents a gateway for Nano.
    """

    MONERO = "MONERO"
    """
    Represents a gateway for Monero.
    """

    SOLANA = "SOLANA"
    """
    Represents a gateway for Solana.
    """

    RIPPLE = "RIPPLE"
    """
    Represents a gateway for Ripple.
    """

    BINANCE_COIN = "BINANCE_COIN"
    """
    Represents a gateway for Binance Coin.
    """

    USDC = "USDC"
    """
    Represents a gateway for USD Coin (USDC).
    """

    USDT = "USDT"
    """
    Represents a gateway for Tether (USDT).
    """

    TRON = "TRON"
    """
    Represents a gateway for TRON.
    """

    BITCOIN_LN = "BITCOIN_LN"
    """
    Represents a gateway for Lightning Network Bitcoin.
    """

    CONCORDIUM = "CONCORDIUM"
    """
    Represents a gateway for Concordium.
    """

    POLYGON = "POLYGON"
    """
    Represents a gateway for Polygon.
    """

    PEPE = "PEPE"
    """
    Represents a gateway for Pepe.
    """

    DAI = "DAI"
    """
    Represents a gateway for Dai.
    """

    WETH = "WETH"
    """
    Represents a gateway for Wrapped Ethereum (WETH).
    """

    APE = "APE"
    """
    Represents a gateway for Ape.
    """

    SHIB = "SHIB"
    """
    Represents a gateway for Shiba Inu (SHIB).
    """

    USDC_NATIVE = "USDC_NATIVE"
    """
    Represents a gateway for Native USD Coin (USDC).
    """

    DOGECOIN = "DOGECOIN"
    """
    Represents a gateway for Dogecoin.
    """

    PYTH = "PYTH"
    """
    Represents a gateway for Pyth.
    """

    BONK = "BONK"
    """
    Represents a gateway for Bonk.
    """

    JUP = "JUP"
    """
    Represents a gateway for Jupiter.
    """

    JITO = "JITO"
    """
    Represents a gateway for Jito.
    """

    WEN = "WEN"
    """
    Represents a gateway for Wen.
    """

    RENDER = "RENDER"
    """
    Represents a gateway for Render.
    """

    MOBILE = "MOBILE"
    """
    Represents a gateway for Mobile payments.
    """

    HNT = "HNT"
    """
    Represents a gateway for Helium (HNT).
    """
    
class Blockchain(Enum):
    """
    Enum representing the blockchain for orders.
    """

    ERC20 = "ERC20"
    """
    Represents a blockchain for ERC20 tokens.
    """

    BEP20 = "BEP20"
    """
    Represents a blockchain for BEP20 tokens.
    """

    TRC20 = "TRC20"
    """
    Represents a blockchain for TRC20 tokens.
    """

    MATIC = "MATIC"
    """
    Represents a blockchain for Polygon (formerly Matic).
    """

    SOL = "SOL"
    """
    Represents a blockchain for Solana.
    """
   
class StripeAPM(Enum):
    """
    Enum representing alternative payment methods for Stripe.
    """

    AFTERPAY_CLEARPAY = "AFTERPAY_CLEARPAY"
    """
    Represents an alternative payment method for Afterpay/Clearpay.
    """

    ALIPAY = "ALIPAY"
    """
    Represents an alternative payment method for Alipay.
    """

    BANCONTACT = "BANCONTACT"
    """
    Represents an alternative payment method for Bancontact.
    """

    AU_BECS_DEBIT = "AU_BECS_DEBIT"
    """
    Represents an alternative payment method for AU BECS Debit.
    """

    BOLETO = "BOLETO"
    """
    Represents an alternative payment method for Boleto.
    """

    EPS = "EPS"
    """
    Represents an alternative payment method for EPS.
    """

    FPX = "FPX"
    """
    Represents an alternative payment method for FPX.
    """

    GIROPAY = "GIROPAY"
    """
    Represents an alternative payment method for Giropay.
    """

    GRABPAY = "GRABPAY"
    """
    Represents an alternative payment method for GrabPay.
    """

    IDEAL = "IDEAL"
    """
    Represents an alternative payment method for iDEAL.
    """

    KLARNA = "KLARNA"
    """
    Represents an alternative payment method for Klarna.
    """

    OXXO = "OXXO"
    """
    Represents an alternative payment method for OXXO.
    """

    P24 = "P24"
    """
    Represents an alternative payment method for P24.
    """

    SOFORT = "SOFORT"
    """
    Represents an alternative payment method for Sofort.
    """

    WECHAT_PAY = "WECHAT_PAY"
    """
    Represents an alternative payment method for WeChat Pay.
    """

class Status(Enum):
    """
    Enum representing the status of an order.
    """

    PENDING = "PENDING"
    """
    Represents a pending order status.
    """

    COMPLETED = "COMPLETED"
    """
    Represents a completed order status.
    """

    VOIDED = "VOIDED"
    """
    Represents a voided order status.
    """

    WAITING_FOR_CONFIRMATIONS = "WAITING_FOR_CONFIRMATIONS"
    """
    Represents an order status waiting for confirmations.
    """

    PARTIAL = "PARTIAL"
    """
    Represents a partial order status.
    """

    CUSTOMER_DISPUTE_ONGOING = "CUSTOMER_DISPUTE_ONGOING"
    """
    Represents an order status with an ongoing customer dispute.
    """

    REVERSED = "REVERSED"
    """
    Represents a reversed order status.
    """

    REFUNDED = "REFUNDED"
    """
    Represents a refunded order status.
    """

    WAITING_SHOP_ACTION = "WAITING_SHOP_ACTION"
    """
    Represents an order status waiting for shop action.
    """

    PROCESSING = "PROCESSING"
    """
    Represents a processing order status.
    """

class STAT_DETAILS(Enum):
    """
    Enum representing the status_details of an order.
    """
    STATUS_DETAILS = "STATUS_DETAILS"
    """
    Represents status details.
    """

class VOID_DETAILS(Enum):
    """
    Enum representing the void_details of an order.
    """
    PRODUCT_SOLD_OUT = "PRODUCT_SOLD_OUT"
    """
    Represents product sold out.
    """
    CART_PRODUCTS_SOLD_OUT = "CART_PRODUCTS_SOLD_OUT"
    """
    Represents cart product sold out.
    """
