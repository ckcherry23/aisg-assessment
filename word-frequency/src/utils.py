"""Module containing utility functions."""


def ordinal(n: int) -> str:
    """
    Convert an integer into its ordinal representation.

    Args:
        n (int): The integer to be converted into its ordinal representation.

    Returns:
        str: The ordinal representation of the input integer.

    Examples:
        >>> ordinal(1)
        '1st'
        >>> ordinal(3)
        '3rd'
        >>> ordinal(11)
        '11th'
        >>> ordinal(22)
        '22nd'
    """
    # Reference: https://stackoverflow.com/a/50992575/15226661
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return str(n) + suffix
