#!/usr/bin/python3
"""class my list
"""


class MyList(list):
    """Mylist
    """
    def print_sorted(self):
        """
        print list in sorted
        """
        list_sorted = sorted(self)
        print(list_sorted)
