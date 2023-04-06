#!/usr/bin/python3
"""
this defines an integer addition function.
"""
def add_integer(a, b=98):
    """ this function returns the integer addition of a and b.

    Args:
        a: first argument
        b: second argument
    Returns:
        sum of the two arguments

    Raises:
        TypeError: if either of the args not an integer or float
    """

    if(not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")
    #cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
    
