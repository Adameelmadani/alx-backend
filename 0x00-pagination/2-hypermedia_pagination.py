#!/usr/bin/env python3
"""
This is our module
"""
import csv
import math
from typing import Tuple, List
"""
These are some modules
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This is our function
    """
    my_tuple: Tuple[int, int] = (page_size * (page - 1), page_size * page)
    return my_tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This is get_page function
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        my_tuple: Tuple[int, int] = index_range(page, page_size)
        length = len(self.dataset())
        if my_tuple[0] >= length or my_tuple[1] >= length:
            return []
        return self.dataset()[my_tuple[0]:my_tuple[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This is het_hyper function
        """
        datas = self.get_page(page, page_size)
        my_dict = {}
        my_dict["page_size"] = page_size
        my_dict["page"] = page
        my_dict["data"] = datas
        my_dict["next_page"] = page + 1
        if self.get_page(page + 1, page_size) == []:
            my_dict["next_page"] = None
        my_dict["prev_page"] = page - 1
        if page == 1:
            my_dict["prev_page"] = None
        my_dict["total_pages"] = int(len(self.dataset()) / page_size)
        return my_dict
