#!/usr/bin/env python3
"""
This is our python module
"""
BaseCaching = __import__("base_caching").BaseCaching
"""
BaseCaching class
"""


class BasicCache(BaseCaching):
    """
    This is our BasicCache class
    """
    def __init__(self):
        """
        This is the constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        This is our put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        This is our get method
        """
        if key is None:
            return None
        return self.cache_data.get(key)
