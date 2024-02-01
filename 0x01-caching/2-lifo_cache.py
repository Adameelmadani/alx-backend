#!/usr/bin/env python3
"""
This is our python module
"""
BaseCaching = __import__("base_caching").BaseCaching
"""
BaseCaching class
"""


class LIFOCache(BaseCaching):
    """
    This is our LIFOCache class
    """
    def __init__(self):
        """
        This is the constructor
        """
        super().__init__()
        self.lifo_list = []

    def put(self, key, item):
        """
        This is our put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        else:
            return
        if len(self.cache_data) > super().MAX_ITEMS:
            print("DISCARD:", self.lifo_list[-1])
            self.cache_data.pop(self.lifo_list[-1])
            self.lifo_list.pop(-1)
        self.lifo_list.append(key)

    def get(self, key):
        """
        This is our get method
        """
        if key is None:
            return None
        return self.cache_data.get(key)
