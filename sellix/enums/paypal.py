from enum import (
    Enum,
)


class PayPalDisputes(
    Enum
):
    MERCHANDISE_OR_SERVICE_NOT_RECEIVED = "The customer did not receive the merchandise or service."
    MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED = "The customer reports that the merchandise or service is not as described."
    UNAUTHORISED = "The customer did not authorize the purchase of the merchandise or service."
    CREDIT_NOT_PROCESSED = "The refund or credit was not processed for the customer."
    DUPLICATE_TRANSACTION = "The transaction was a duplicate."
    INCORRECT_AMOUNT = "The customer was charged an incorrect amount."
    PAYMENT_BY_OTHER_MEANS = "The customer paid for the transaction through other means."
    CANCELED_RECURRING_BILLING = "The customer was being charged for a subscription or a recurring transaction that was canceled."
    PROBLEM_WITH_REMITTANCE = "A problem occurred with the remittance."
    OTHER = "Other."


class DisputeStatus(
    Enum
):
    OPEN = "The dispute is open."
    WAITING_FOR_BUYER_RESPONSE = "The dispute is waiting for a response from the customer."
    WAITING_FOR_SELLER_RESPONSE = "The dispute is waiting for a response from the merchant."
    UNDER_REVIEW = "The dispute is under review with PayPal."
    RESOLVED = "The dispute is resolved."
    OTHER = "The default status if the dispute does not have one of the other statuses."


class DisputeOutcome(
    Enum
):
    RESOLVED_BUYER_FAVOUR = "The dispute was resolved in the customer’s favor."
    RESOLVED_SELLER_FAVOUR = "The dispute was resolved in the merchant’s favor."
    RESOLVED_WITH_PAYOUT = "PayPal provided the merchant or customer with protection and the case is resolved."
    CANCELED_BY_BUYER = "The customer canceled the dispute."
    ACCEPTED = "PayPal accepted the dispute."
    DENIED = "PayPal denied the dispute."
    NONE = "A dispute was created for the same transaction ID, and the previous dispute was closed without any decision."


class DisputeLifeCycle(
    Enum
):
    INQUIRY = "A customer and merchant interact in an attempt to resolve a dispute without escalation to PayPal. Occurs when the customer: Has not received goods or a service. Reports that the received goods or services are not as described. Needs more details, such as a copy of the transaction or a receipt."
    CHARGEBACK = "A customer or merchant escalates an inquiry to a claim, which authorizes PayPal to investigate the case and make a determination. Occurs only when the dispute channel is INTERNAL. This stage is a PayPal dispute lifecycle stage and not a credit card or debit card chargeback. All notes that the customer sends in this stage are visible to PayPal agents only. The customer must wait for PayPal's response before the customer can take further action. In this stage, PayPal shares dispute details with the merchant, who can complete one of these actions: accept the claim, submit evidence to challenge the claim, make an offer to the customer to resolve the claim."
    PRE_ARBITRATION = "The first appeal stage for merchants. A merchant can appeal a chargeback if PayPal's decision is not in the merchant's favor. If the merchant does not appeal within the appeal period, PayPal considers the case resolved."
    ARBITRATION = "The second appeal stage for merchants. A merchant can appeal a dispute for a second time if the first appeal was denied. If the merchant does not appeal within the appeal period, the case returns to a resolved status in a pre-arbitration stage."


class DisputeMessagePostedBy(
    Enum
):
    """
    Class representing the initiator of the dispute message.
    """

    BUYER = "The customer posted the message."
    SELLER = "The merchant posted the message."
    ARBITER = "The arbiter of the dispute posted the message."
