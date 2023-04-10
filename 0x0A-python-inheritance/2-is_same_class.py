#!/usr/bin/python3
"""Defines a class instance chacking"""

def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
