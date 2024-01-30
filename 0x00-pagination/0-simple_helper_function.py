#!/usr/bin/env python3
"""
This is our module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This is our function
    """
    my_tuple: Tuple[int, int] = (page_size * (page - 1), page_size * page)
    return my_tuple
