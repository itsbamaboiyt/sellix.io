from ..enums.caller import (
    ShopType,
    Currency,
    DashboardFeature,
    SortCustomTheme,
    DefaultSort,
    OrderOrigin, 
    OrderSubtype, 
    OrderType,
    ProductType,
    Gateway,
    Blockchain,
    StripeAPM,
    Status,
    STAT_DETAILS,
    VOID_DETAILS


)
from ..enums.checkables import (
    DisplayTaxOnStorefront,
    DisplayTaxCustomFields,
    ValidationOnlyForCompanies,
    ValidateVatNumber,
    PricesTaxInclusive,
    NotifySubscriptionRenewalFailure,
    NotifyTrialEnding,
    NotifyUpcomingRenewal,
    OrderEmails,
    PayPalCreditCard,
    ForcePaypalEmailDelivery,
    NonCustodialWallet,
    DarkMode,
    SearchEnabled,
    SortEnabled,
    CartEnabled,
    HideOutOfStock,
    HideProductsSold,
    HideStockCounter,
    ServiceDateFrom,
    CenterProductTitles,
    CenterGroupTitles,
    CustomTheme,
    CustomEmbed,
    DescriptionYouTubeOnly,
    OnHold,
    Verified,
    DescriptionImage,
    DescriptionSkipDefaultImage,
    SetupWizard,
    SetupCryptocurrencies,
    MarketplaceVerified,
    DarkMode
)


import msgspec
import typing as t


class Shop(
    msgspec.Struct
):
    """
    A class that represents a Sellix `Shop` or `GET self` method on the API.

    ---
    Reference: [sellix.get_self](https://docs.sellix.io/api-reference/information/get-self)
    """

    id: int
    """The ID of the shop"""

    user_id: int
    """The ID of the user who requested the shop info"""

    shop_type: ShopType = msgspec.field(
        name="type"
    )
    """The type of the shop"""

    name: str
    """The name of the shop"""

    avatar: str
    """The [hash](https://www.geeksforgeeks.org/what-is-hashing) for the avatar"""

    currency: Currency
    """Available currency."""

    default_currency: Currency
    """Available currency."""

    available_currency: Currency
    """Available currency."""

    vat_percentage: str
    """The VAT percentage setup for the store"""

    tax_configuration: str
    """The tax configuration for the shop"""

    dashboard_feature: DashboardFeature
    """The organization mode set for the dashboard"""

    display_tax_on_storefront: DisplayTaxOnStorefront
    """The tax percentage will be shown on the product cards of your storefront, and not on the checkout page and invoice PDF only."""

    display_tax_custom_fields: DisplayTaxCustomFields
    """Whether the tax is displayed in custom fields"""

    validation_only_for_companies: ValidationOnlyForCompanies
    """Wheter or not VAT validation is only done for companies"""

    validate_vat_number: ValidateVatNumber
    """If enabled, we will validate the Company VAT number to be sure it's correct."""

    prices_tax_inclusive: PricesTaxInclusive
    """Whether or not product pricing incldues the VAT"""

    notify_trial_ending: NotifyTrialEnding
    """Send an email to your customers when the trial period is ending."""

    notify_upcoming_renewal: NotifyUpcomingRenewal
    """Send an email to your customers days before an upcoming renewal."""

    notify_subscription_renewal_failure: NotifySubscriptionRenewalFailure
    """Send an email to your customers when a subscription renewal fails."""

    order_emails: OrderEmails
    """Whether or not order emails are enabled"""

    subscription_grace_period: int
    """In days, how much time should we wait before cancelling a subscription if no payment is completed."""

    paypal_credit_card: PayPalCreditCard
    """Whether or not the shop accepts credit cards via PayPal"""

    force_paypal_email_delivery: ForcePaypalEmailDelivery
    """Whether or not the shop accepts credit cards via PayPal"""

    paypal_merchant_id: str
    """The PayPal merchant ID of the PayPal account linked to the shop"""

    binance_id: str
    """The Binance ID of the Binance account linked to the shop"""

    walletconnect_id: str
    """The WalletConnect ID of the WalletConnect account linked to the shop"""

    non_custodial_wallet: NonCustodialWallet
    """Whether or not the shop uses the Sellix non-custodial crypto wallet"""

    dark_mode: DarkMode
    """Whether or not the shop is in dark mode"""

    discord_link: str
    """The Discord link of the shop"""

    twitter_link: str
    """The link to the shop's Twitter account"""

    instagram_link: str
    """The link to the shop's Instagram account"""

    facebook_link: str
    """The link to the shop's Facebook account"""

    telegram_link: str
    """The invite link to the shop's Telegram community"""

    youtube_link: str
    """The invite link to the shop's Youtube channel"""

    reddit_link: str
    """The link to the shop's SubReddit"""

    tiktok_link: str
    """The link to the shop's TikTok account"""

    search_enabled: SearchEnabled
    """Whether or not the shop has dark mode enabled"""

    sort_enabled: SortEnabled
    """Whether or not the shop has product sorting enabled"""

    cart_enabled: CartEnabled
    """Whether or not the shop has the cart system enabled"""

    cart_maximum_checkout: str
    """Set the maximum amount, in your currency, for an order made through the Shopping Cart."""

    hide_out_of_stock: HideOutOfStock
    """Automatically hide your products when out of stock."""

    google_analytics_tracking_id: str
    """The google analyticd tracking id the shop uses for analytics"""

    crisp_website_id: str
    """The crisp website id the shop uses for analytics"""

    center_product_titles: CenterProductTitles
    """Whether or not the shop's theme centers product titles"""

    center_group_titles: CenterGroupTitles
    """Whether or not the shop's theme centers group titles"""

    popup_message: str
    """This message will be shown to anyone who visits your site. Do not include your Terms of Service here."""

    verified: Verified
    """Whether or not the shop is verified by Sellix"""

    on_hold: OnHold
    """Whether or not the shop is on hold"""

    terms_of_service: str
    """The terms of service for the shop in MDX"""

    primary_color_custom_theme: str
    """The primary color of the shop's custom theme. Value is null if no custom theme is used."""

    secondary_color_custom_theme: str
    """The secondary color of the shop's custom theme. Value is null if no custom theme is used."""

    primary_font_color_custom_theme: str
    """The primary font color of the shop's custom theme. Value is null if no custom theme is used."""

    secondary_font_color_custom_theme: str
    """The secondary font color of the shop's custom theme. Value is null if no custom theme is used."""

    custom_embed: CustomEmbed
    """Whether or not the shop uses a custom embed theme. Value is null if no custom theme is used."""

    custom_theme: CustomTheme
    """Whether or not the shop uses a custom storefront theme. Value is null if no custom theme is used."""

    font_custom_theme: str
    """The font of the shop's custom storefront theme. Value is null if no custom theme is used."""

    style_custom_theme: str
    """The style of the shop's custom storefront theme. Value is null if no custom theme is used."""

    embed_style_custom_theme: str
    """The style of the shop's custom embed theme. Value is null if no custom theme is used."""

    index_custom_theme: str
    """The index of the shop's active custom storefront theme. Value is null if no custom theme is used."""

    product_card_custom_theme: str
    """The product_card of the shop's active custom storefront theme. Value is null if no custom theme is used."""

    banner_custom_theme: object
    """The storefront banner of the shop's custom theme. Value is null if no custom theme is used."""

    footer_custom_theme: object
    """The storefront footer of the shop's custom theme. Value is null if no custom theme is used."""

    background_image_custom_theme: object
    """The storefront background image of the shop's custom theme. Value is null if no custom theme is used."""

    logo_custom_theme: object
    """The storefront logo of the shop's custom theme. Value is null if no custom theme is used."""

    header_custom_theme: object
    """The storefront header of the shop's custom theme. Value is null if no custom theme is used."""

    cards_in_row_custom_theme: int
    """The amount of cards to display in a row on the storefront"""

    cards_align_custom_theme: object
    """Value is null if no custom theme is used."""

    group_card_custom_theme: object
    """Value is null if no custom theme is used."""

    card_animation_custom_theme: object
    """Value is null if no custom theme is used."""

    light_font_color_custom_theme: str
    """The light mode font color of the shop's custom theme. Value is null if no custom theme is used."""

    dark_font_color_custom_theme: str
    """The dark mode font color of the shop's custom theme. Value is null if no custom theme is used."""

    light_color_custom_theme: str
    """light_color_custom_theme"""

    dark_color_custom_theme: str
    """The dark mode accent color of the shop's custom theme. Value is null if no custom theme is used."""

    border_color_custom_theme: str
    """The border color of the shop's custom theme. Value is null if no custom theme is used."""

    button_color_custom_theme: str
    """The button color of the shop's custom theme. Value is null if no custom theme is used."""

    thin_color_custom_theme: str
    """The thin font color of the shop's custom theme. Value is null if no custom theme is used."""

    sort_custom_theme: SortCustomTheme
    """The default sorting method for the storefront's custom theme"""

    helpspace_client_id: str
    """The helpspace client id of the helpspace account linked to the shop"""

    helpspace_token: str
    """The helpspace token of the helpspace account linked to the shop"""

    description_youtube_only: DescriptionYouTubeOnly
    """Show only youtube video for invoice/product description."""

    description_skip_default_image: DescriptionSkipDefaultImage
    """Skip Default Image for Product Description."""

    hide_stock_counter: HideStockCounter
    """If enabled, the number of how many products are in stock will be removed, we will only show 'In Stock' or 'Out of Stock'."""

    image_width: int
    """The width of the storefront image"""

    image_height: int
    """The height of the storefront image"""

    default_sort: DefaultSort
    """The default sorting method for the storefront"""

    description_image: DescriptionImage
    """Whether or not the shop has a description image."""

    hide_products_sold: HideProductsSold
    """Hide the products sold counter on your storefront, only your average feedback will be displayed."""

    service_date_from: ServiceDateFrom
    """Choose whether to display your business starting date from the day of your first sale or the day you have signed up to Sellix."""

    cards_type: str
    """`DEPRECATED`: The name of the product image with the file type"""

    setup_wizard: SetupWizard
    """Whether or not the shop has completed the setup wizzard"""

    setup_cryptocurrencies: SetupCryptocurrencies
    """Whether or not the shop has setup cryptocurrencies"""

    notices_banner: str
    """The notices for the shop"""

    affiliate_revenue_percent: int
    """The percentage of each payment given to affiliates"""

    created_at: int
    """Timestamp for the creation of the subscription."""

    image_name: str
    """`DEPRECATED`: The name of the product image with the file type"""

    image_storage: str
    """Where the image is stored in Sellix's self-hosted CDN."""

    cloudflare_image_id: str
    """
    #### New field containing the cloudflare image ID of this product.
    Replaces `image_attachment` and `image_name`.
    Format
    URL: `https://imagedelivery.net/95QNzrEeP7RU5l5WdbyrKw/<cloudflare_image_id>/<variant_name>`
    Where `variant_name` can be `shopItem`, `avatar`, `icon`, `imageAvatarFeedback`, `public`, `productImageCart`.
    """

    marketplace_verified: MarketplaceVerified
    """Whether or not the shop is a verified marketplace"""


class Order(msgspec.Struct):
    id: int
    """ID of the resource."""
    
    uniqid: str
    """Unique ID of the resource, used as reference across the API."""
    
    recurring_billing_id: str
    """Unique ID of the recurring bill."""
    
    payout_configuration: str
    """`DEPRECATED`"""
    
    type: OrderType
    """Invoice type. For subscriptions, the invoice type is PRODUCT_SUBSCRIPTION as SUBSCRIPTION is reserved for Sellix-own plans."""
    
    subtype: OrderSubtype
    """Product type."""
    

    origin: OrderOrigin
    """How the invoice was created"""
    
    total: float
    """Invoice total, unit_price*quantity where quantity is applicable."""
    
    total_display: float
    """Invoice total in the currency chosen."""
    
    exchange_rate: float
    """Exchange rate between currency chosen and USD."""
    
    crypto_exchange_rate: float
    """Exchange rate between the cryptocurrency chosen (if any) and USD."""
    
    currency: Currency
    """Available currency."""
    
    shop_id: int
    """The shop ID to which this invoice belongs."""
    
    
    shop_image_name: str
    """`DEPRECATED`: Unique id of the image attachment for this merchant with the image extension included."""
    
    shop_image_storage: str
    """Where the image is stored in Sellix's self-hosted CDN."""
    
    cloudflare_image_id: str
    """New field containing the cloudflare image ID of this product."""
    name: str
    """Name of the merchant."""
    customer_email: str
    """Email of the customer."""
    customer_id: str
    """ID of the customer."""
    affliate_revenue_customer_id: str
    """ID of the affiliate"""
    paypal_email_delivery: bool
    """If true and gateway is PAYPAL, the product will be shipped to the PayPal email 
    on record instead of the customer email."""
    product_id: str
    """Unique ID of the product linked to this invoice, if any."""
    product_title: str
    """Product title."""
    product_type: ProductType
    """Product type."""
    subscription_id: int
    """Field reserved for Sellix-own plans. Unique ID of the subscription purchased."""

    subscription_time: int
    """Field reserved for Sellix-own plans. Time, in seconds, of the subscription purchased."""
    gateway: Gateway
    """Gateway chosen for this invoice. """
    blockchain: Blockchain
    """The blockchain of the crypto currency."""
    paypal_apm: str
    """PayPal Alternative Payment Method name, such as iDEAL, used if gateway is PAYPAL."""
    stripe_apm: StripeAPM
    """Stripe Alternative Payment Method name, such as iDEAL, used if gateway is STRIPE."""
    paypal_email: str
    """Merchant PayPal email"""

    paypal_order_id: str
    """This field contains the PayPal order ID."""

    paypal_payer_email: str
    """This field is updated after the invoice is completed with the PayPal's email used for the purchase."""
    paypal_fee: int
    """This field is updated after the invoice is completed with the fee taken by PayPal over the invoice total."""
    paypal_subscription_id: int
    """ID of the paypal subscription."""
    paypal_subscription_link: int
    """Link for the merchant to purchase the subscription from."""
    lex_order_id: str
    """DEPRECATED"""
    lex_payment_method: str
    """DEPRECATED"""
    paydash_paymentID: str
    """DEPRECATED"""
    virtual_payments_id: str
    """DEPRECATED"""
    stripe_client_secret: str
    """Client secret used to create the STRIPE paymentIntent."""
    stripe_price_id: str
    """If the invoice type is PRODUCT_SUBSCRIPTION or SUBSCRIPTION, refers to the STRIPE price ID."""
    skrill_email: str
    """Merchant Skrill email."""
    skrill_sid: str
    """Skrill unique ID linked to the invoice."""
    skrill_link: str
    """Skrill link to redirect the customer to."""
    perfectmoney_id: str
    """PerfectMoney payment ID linked to the invoice."""
    binance_invoice_id: str
    """ID for binance invoice"""
    binance_qrcode: str
    """Full Binance QRCODE string"""
    binance_checkout_url: str
    """Checkout URL for Binance invoice"""
    crypto_address: str
    """Cryptocurrency address linked to this invoice."""
    crypto_amount: float
    """Cryptocurrency amount converted based on crypto_exchange_rate."""
    crypto_received: float
    """Cryptocurrency amount received, paid by the customer."""
    crypto_uri: str
    """URI used to create the QRCODE."""
    crypto_confirmations_needed: int
    """Crypto confirmations needed to process the invoice"""
    crypto_scheduled_payout: bool
    """If true, a scheduled payout for this invoice's cryptocurrency address has been sent."""
    crypto_payout: bool
    """If true, an instant payout for this invoice's cryptocurrency address has been sent."""
    fee_billed: bool
    """If true, the Sellix fee_percentage has already been collected."""
    cashapp_qrcode: str
    """Full CashApp QRCODE string."""
    cashapp_note: str
    """Unique note for the customer to leave in the CashApp payment."""
    cashapp_cashtag: str
    """CashApp cashtag used to create the QRCODE."""
    country: str
    """Customer country."""
    location: str
    """Customer location"""
    ip: str
    """Customer IP."""
    is_vpn_or_proxy: bool
    """If true, a VPN or Proxy has been detected."""
    user_agent: str
    """Customer User Agent."""
    quantity: int
    """Qauntity of product purchased."""
    coupon_id: str
    """Unique ID of the coupon, if used, for the discount."""
    developer_invoice: bool
    """If true, this invoice has been created through the Developers API."""
    developer_title: str
    """If a product_id is not passed through the Developers API, a title must be specified."""
    developer_webhook: str
    """Additional webhook URL to which updates regarding this invoice will be sent."""
    developer_return_url: str
    """If present, the customer will be redirected to this URL after the invoice has been paid."""
    status: str
    """Status of the invoice."""
    status_details: STAT_DETAILS
    """If CART_PARTIAL_OUT_OF_STOCK, the invoice has been completed but some products in the cart were out of stock."""
    void_details: VOID_DETAILS
    """"""
    discount: int
    """If a coupon or volume_discount is used, the discount value presents the total amount of discount over the total cost of the invoice."""
    fee_percentage: int 
    """What cut does Sellix take out of the total."""
    day_value: int
    """DEPRECATED: Day value, number."""
    day: str
    """DEPRECATED: First three letters of the day name."""
    month: str
    """DEPRECATED: First three letters of the month name."""
    year: int
    """DEPRECATED: Year number."""
    created_at: int
    """Timestamp for the creation of the invoice."""
    updated_at: int
    """Date, available if the blacklist has been edited."""
    updated_by: int
    """User ID of the user who updated the invoice."""
    service_text: str
    """If the product type is SERVICE, this field contains additional details on the type of service provided by the merchant."""
    payment_link_id: str
    """The ID for the payment link, if invoice was created by a payment link"""
    cashapp_email_configured: bool
    """Whether or not cashapp email is configured"""
    license: bool
    """True if the product is of type LICENSE"""
    total_conversions: t.Any
    """"""
    theme: str
    """What Sellix theme the shop is set to."""
    dark_mode: int
    """1 if darkmode is enabled, 0 if it is disabled."""
    crypto_mode: t.Any
    """"""
    country_regulations: str
    """The country the shop is opperated in"""
    shop_paypal_credit_card: bool
    """If true, the merchant has enabled purchase with Credit Card through PayPal."""
    shop_force_paypal_email_delivery: bool
    """If true, the merchant has enabled invoice shipment to the PayPal customer email."""
    shop_walletconnect_id: t.Any
    """"""
    original_developer_return_url: str
    """The original return url of the order."""
