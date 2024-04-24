from ..enums.caller import (
    ShopType,
    Currency,
    DashboardFeature,
    SortCustomTheme,
    DefaultSort,
    OrderOrigin, 
    OrderSubtype, 
    OrderType
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
)


import msgspec


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
    customer_email: str
    customer_id: str
    affliate_revenue_customer_id: str
    paypal_email_delivery: bool
    product_id: str
    product_title: str
    product_type: str
    subscription_id: int
    subscription_time: int
    gateway: str
    blockchain: str
    paypal_apm: str
    stripe_apm: str
    paypal_email: str
    paypal_order_id: str
    paypal_payer_email: str
    paypal_fee: int
    paypal_subscription_id: int
    paypal_subscription_link: int
    lex_order_id: str
    lex_payment_method: str
    paydash_paymentID: str
    virtual_payments_id: str
    stripe_client_secret: str
    stripe_price_id: str
    skrill_email: str
    skrill_sid: str
    skrill_link: str
    perfectmoney_id: str
    binance_invoice_id: str
    binance_qrcode: str
    binance_checkout_url: str
    crypto_address: str
    crypto_amount: float
    crypto_received: float
    crypto_uri: str
    crypto_confirmations_needed: int
    crypto_scheduled_payout: bool
    crypto_payout: bool
    fee_billed: bool
    cashapp_qrcode: str
    cashapp_note: str
    cashapp_cashtag: str
    country: str
    location: str
    ip: str
    is_vpn_or_proxy: bool
    user_agent: str
    quantity: int
    coupon_id: str
    developer_invoice: bool
    developer_title: str
    developer_webhook: str
    developer_return_url: str
    status: str
    status_details: str
    void_details: str
    discount: int
    fee_percentage: int
    day_value: int
    day: str
    month: str
    year: int
    created_at: int
    updated_at: int
    updated_by: int
    service_text: str
    payment_link_id: str
    cashapp_email_configured: bool
    license: bool
    total_conversions: str
    theme: str
    dark_mode: int
    crypto_mode: str
    country_regulations: str
    shop_paypal_credit_card: bool
    shop_force_paypal_email_delivery: bool
    shop_walletconnect_id: str
    original_developer_return_url: str
