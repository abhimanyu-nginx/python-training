#!flask/bin/python

__author__ = "Abhimanyu Nagurkar"
__copyright__ = "Copyright (C) Nginx Inc. All rights reserved."
__license__ = ""
__maintainer__ = "Abhimanyu Nagurkar"
__email__ = "abhimanyu.nagurkar@nginx.com"

"""Calculates median of any given list"""
def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
