#!/bin/env python
# -*- coding: utf8 -*-

from time import sleep


def z(variable, value, delay=5):
    """ Takes a variable, a value, and a delay in seconds. """
    while variable != value:
        sleep(delay)
