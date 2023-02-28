"""Ütils"""
__author__ = "730614170"

def all(list_var: list(int),x: int) -> bool:
    """Is X = to every nummber in the list"""
    idx: int = 0
    while idx < len(list_var):
        if list[idx] == x:
            idx =+ 1
        else:
            return False
        if idx == len(list_var) - 1:
            return True
        
def max(list_in: list(int)) -> int:
    """Returns largest"""
    if len(input) == 0:
        raise ValueError ("max() arg is an empty List")
    idx: int = 1
    while len(list_in) > 1:
        if list_in[0] > list_in[idx]:
            list_in.pop(idx)
        else:
            list_in.pop(0)
    return list_in[0]


def is_equal(list1: list(int), list2: list(int)) -> bool:
    """compare two lists"""
    idx: int = 0
    idx2: int = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1):
        if list1[idx] == list2[idx]:
            idx =+ 1
        else:
            return False
    return  True
