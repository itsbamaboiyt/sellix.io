from enum import Enum


class MerchantTier(Enum):
    """
    A class representing all the given tiers according to Sellix.

    To upgrade to a higher tier, please reach out to us at [sales@sellix.io](mailto:sales@sellix.io) or through our [Discord community](https://sellix.io/discord).

    ---
    Reference: [sellix.tier](https://docs.sellix.io/api-reference/errors#general-endpoints)
    """

    STANDARD = "Standard", 5
    """
    Standard sellix tier allows general rate-limit of 5 requests, per 10s.
    - `STANDARD`: Represents the standard tier with a value of 5.
    """

    TIER_1 = "Tier 1", 75
    """
    Represents Tier 1 with a rate-limit of 75 requests per 10s.
    - `TIER_1`: Represents Tier 1 with a rate-limit of 75.
    """

    TIER_2 = "Tier 2", 100
    """
    Represents Tier 2 with a rate-limit of 100 requests per 10s.
    - `TIER_2`: Represents Tier 2 with a rate-limit of 100.
    """

    TIER_3 = "Tier 3", 500
    """
    Represents Tier 3 with a rate-limit of 500 requests per 10s.
    - `TIER_3`: Represents Tier 3 with a rate-limit of 500.
    """


class WebHookEvents(Enum):
    """
    A class representing all the `webhook` events.

    ---
    Reference: [sellix.webhooks](https://docs.sellix.io/api-reference/webhooks#events)
    """

    ORDER_CREATED = "order:created", "The order has been created."
    """Event triggered when an order is created."""

    ORDER_UPDATED = "order:updated", "The order status has changed."
    """Event triggered when the order status is updated."""

    ORDER_PARTIAL = (
        "order:partial",
        "The order status is now partial, indicating a cryptocurrency payment that has been sent but not covering the whole amount.",
    )
    """Event triggered when the order status becomes partial."""

    ORDER_PAID = (
        "order:paid",
        "The order has been flagged as paid, this is the final state.",
    )
    """Event triggered when the order is marked as paid."""

    ORDER_CANCELLED = (
        "order:cancelled",
        "The order has been cancelled either by the fraud shield, the merchant, or due to not receiving a payment within the time window.",
    )
    """Event triggered when the order is cancelled."""

    ORDER_DISPUTED = (
        "order:disputed",
        "A Stripe/PayPal dispute has been opened against one of your stores.",
    )
    """Event triggered when a dispute is opened against an order."""

    PRODUCT_CREATED = "product:created", "A product has been created."
    """Event triggered when a product is created."""

    PRODUCT_STOCK = (
        "product:stock",
        "A product’s stock has fallen below the warning range.",
    )
    """Event triggered when a product's stock falls below the warning range."""

    PRODUCT_EDITED = "product:edited", "A product has been edited."
    """Event triggered when a product is edited."""

    PRODUCT_DYNAMIC = (
        "product:dynamic",
        "This event is issued only for dynamic products.",
    )
    """Event issued only for dynamic products."""

    QUERY_CREATED = "query:created", "A query has been created for one of your shops."
    """Event triggered when a query is created."""

    QUERY_REPLIED = (
        "query:replied",
        "A reply has been received for one of your queries.",
    )
    """Event triggered when a reply is received for a query."""

    FEEDBACK_RECEIVED = (
        "feedback:received",
        "One of your customers left a feedback for you.",
    )
    """Event triggered when a feedback is received."""

    SUBSCRIPTION_TRIAL_STARTED = (
        "subscription:trial:started",
        "A trial has been started for one of your subscriptions.",
    )
    """Event triggered when a trial is started for a subscription."""

    SUBSCRIPTION_TRIAL_ENDED = (
        "subscription:trial:ended",
        "A trial has ended for one of your subscriptions, this is usually followed by an order:created event.",
    )
    """Event triggered when a trial ends for a subscription."""

    SUBSCRIPTION_CREATED = "subscription:created", "A subscription has been created."
    """Event triggered when a subscription is created."""

    SUBSCRIPTION_UPDATED = "subscription:updated", "A subscription has been updated."
    """Event triggered when a subscription is updated."""

    SUBSCRIPTION_RENEWED = (
        "subscription:renewed",
        "A subscription has been renewed, after receiving a new payment.",
    )
    """Event triggered when a subscription is renewed."""

    SUBSCRIPTION_CANCELLED = (
        "subscription:cancelled",
        "A subscription has been canceled, either due to not receiving a payment or by a manual action of the customer.",
    )
    """Event triggered when a subscription is cancelled."""

    SUBSCRIPTION_UPCOMING = (
        "subscription:upcoming",
        "A customer will have to pay for one of your subscriptions in the next 72 hours.",
    )
    """Event triggered when a subscription payment is upcoming."""

    ORDER_PAID_PRODUCT = (
        "order:paid:product",
        "This event is the same as order:paid, however the :product segment indicates that it originates from a webhook URL configured within a product, which is now deprecated.",
    )
    """Event triggered when an order is paid through a product webhook URL."""

    ORDER_PARTIAL_PRODUCT = (
        "order:partial:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order status is partial through a product webhook URL."""

    ORDER_CREATED_PRODUCT = (
        "order:created:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order is created through a product webhook URL."""

    ORDER_DISPUTED_PRODUCT = (
        "order:disputed:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order is disputed through a product webhook URL."""

    ORDER_CANCELLED_PRODUCT = (
        "order:cancelled:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order is cancelled through a product webhook URL."""

    ORDER_UPDATED_PRODUCT = (
        "order:updated:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order status is updated through a product webhook URL."""


class LinkStep(Enum):
    """
    A class representing the available step number to be configured on links.

    ---
    Reference: [sellix.prefilledlinks](https://docs.sellix.io/api-reference/prefilled-links#available-querystring-parameters)
    """

    DEFAULT_CHECKOUT = 0
    """The default checkout step (product details)"""
    GATEWAY_CHOICE = 1
    """The gateway choice step"""
    EMAIL_AND_PAY_BUTTON = 3
    """The email and pay button step"""


