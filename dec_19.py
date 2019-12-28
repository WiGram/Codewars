# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 22:08:53 2019

@author: willi
"""


s = "the-stealth-warrior"

def to_camel_case(text):
    """
    

    Parameters
    ----------
    text : string
        A string of words delimited by either '-' or '_'

    Returns
    -------
    string
        A string with no delimiter, where all words after the first are capitalised.

    """
    t = s.replace('_','-').split('-')
    return ''.join([s.capitalize() if i > 0 else s for i, s in enumerate(t)])

