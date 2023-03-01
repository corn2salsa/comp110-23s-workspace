"""Ütils."""
__author__ = "730614170"


def all(a_list: list[int], x: int) -> bool:
    """Is X = to every nummber in the list."""
    idx: int = 0
    while idx < len(a_list):
        if a_list[idx] == x:
            idx = idx + 1
        else:
            return False
        if idx == len(a_list) - 1:
            return True
    return False
        

def max(list_in: list[int]) -> int:
    """Returns largest."""
    if len(list_in) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 1
    while len(list_in) > 1:
        if list_in[0] > list_in[idx]:
            list_in.pop(idx)
        else:
            list_in.pop(0)
    return list_in[0]


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Compare two lists."""
    idx: int = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1):
        if list1[idx] == list2[idx]:
            idx = idx + 1
        else:
            return False
    return True
