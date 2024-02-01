#!/usr/bin/env python3
"""
This is our python module
"""
BaseCaching = __import__("base_caching").BaseCaching
"""
BaseCaching class
"""


class MRUCache(BaseCaching):
    """
    This is our MRUCache class
    """
    def __init__(self):
        """
        This is the constructor
        """
        super().__init__()
        self.mru_list = []

    def put(self, key, item):
        """
        This is our put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        else:
            return
        if key in self.lru_list:
            self.lru_list.remove(key)
        elif len(self.cache_data) > super().MAX_ITEMS:
            print("DISCARD:", self.lru_list[-1])
            self.cache_data.pop(self.lru_list[-1])
            self.lru_list.pop(-1)
        self.lru_list.append(key)

    def get(self, key):
        """
        This is our get method
        """
        if key is None:
            return None
        return self.cache_data.get(key)
