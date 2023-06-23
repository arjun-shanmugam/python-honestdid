import math
from typing import Type, Union


def square(x: Union[int, float]) -> Union[int, float]:
    """Returns the square of input x.
    Parameters
    ----------
    x : Union[int, float]
        An int or float, to be squared
    Returns
    -------
    Union[int, float]
        The square of input x
    Raises
    ------
    TypeError
        When input x is not an int or float
    Examples
    --------
    >>> square(2)
    4
    >>> square(5)
    25
    >>> square('text')
    TypeError: x should be of type int or float but is of: <class 'str'>
    """
    if not isinstance(x, (int, float)):
        raise TypeError(
            f"x should be of type int or float but is of: {type(x)}"
        )
    elif math.isnan(x):
        raise ValueError(f"x cannot be nan")
    else:
        return x * x
