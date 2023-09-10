#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        return 0, 0
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        return tuple_a[:1] + tuple_b[:1]
    else:
        firstelement = tuple_a[0] + tuple_b[0]
        secondelement = tuple_a[1] + tuple_b[1]
    return firstelement, secondelement
