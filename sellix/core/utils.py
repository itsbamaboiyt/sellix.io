from ..abc.enums import (
    LinkStep,
)
import typing as t


def if_int(
    value: t.Any,
) -> bool:
    """
    Checks if the input value is an integer.

    Args:
    value: The value to check.

    Returns:
    bool: True if the value is an integer, False otherwise.
    """

    return isinstance(
        value,
        int,
    )


def if_bool(
    value: t.Any,
) -> t.Optional[
    bool
]:
    """
    Checks if the input value is a boolean representation.

    Args:
        value: The value to check.

    Returns:
        Optional[bool]: True if the value is "true", False if the value is "false", None otherwise.
    """

    if (
        value
        == "false"
    ):
        return False
    elif (
        value
        == "true"
    ):
        return True
    else:
        return None


def generate_prefilled_link(
    domain: str,
    product_slug: str,
    quantity: t.Optional[
        int
    ] = None,
    gateway: t.Optional[
        str
    ] = None,
    step: t.Optional[
        t.Union[
            t.Literal[
                0,
                1,
                3,
            ],
            LinkStep,
        ]
    ] = None,
    email: t.Optional[
        str
    ] = None,
    coupon_code: t.Optional[
        str
    ] = None,
) -> str:
    """
    Generates a prefilled link for a product with optional parameters.

    Args:
        domain: The domain for the link.
        product_slug: The product slug for the link.
        quantity: The quantity of the product.
        gateway: The gateway for the link.
        step: The step for the link.
        email: The email for the link.
        coupon_code: The coupon code for the link.

    Returns:
        str: The generated prefilled link.
    """

    link = f"https://{domain}/product/{product_slug}?"

    if (
        quantity
        is not None
    ):
        link += f"quantity={quantity}&"

    if (
        gateway
        is not None
    ):
        link += f"gateway={gateway}&"

    if (
        step
        is not None
    ):
        link += f"step={step}&"

    if (
        email
        is not None
    ):
        link += f"email={email}&"

    if (
        coupon_code
        is not None
    ):
        link += f"couponCode={coupon_code}&"

    return link.rstrip(
        "&"
    )
