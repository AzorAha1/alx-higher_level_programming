#!/usr/bin/python3
"""class
"""


class MyInt(int):
    """MyInt
    """
    def __eq__(self, value):
        if not isinstance(value, int):
            return super().__eq__(value)
        return False

    def __ne__(self, value):
        if not isinstance(value, int):
            return super().__ne__(value)
        return True
