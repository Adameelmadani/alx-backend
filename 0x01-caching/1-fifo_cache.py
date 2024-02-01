#!/usr/bin/env python3
"""
This is our python module
"""
BaseCaching = __import__("base_caching").BaseCaching
"""
BaseCaching class
"""


class FIFOCache(BaseCaching):
    """
    This is our FIFOCache class
    """
    def __init__(self):
        """
        This is the constructor
        """
        super().__init__()
        self.fifo_list = []

    def put(self, key, item):
        """
        This is our put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.fifo_list.append(key)
        else:
            return
        if len(self.cache_data) > super().MAX_ITEMS:
            print("DISCARD:", self.fifo_list[0])
            self.cache_data.pop(self.fifo_list[0])
            self.fifo_list.pop(0)

    def get(self, key):
        """
        This is our get method
        """
        if key is None:
            return None
        return self.cache_data.get(key)
