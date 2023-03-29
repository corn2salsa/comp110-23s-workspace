"""Utils."""
__author__: "730614170"


def only_evens(even: list[int]) -> list[int]:
    """Return only evens."""
    even_new: list[int] = []
    for i in range(len(even)):
        if even[i] % 2 == 0:
            even_new.append(even[i])
    return even_new


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Return aggregated list."""
    new_list: list[int] = []
    for i in range(len(list1)):
        new_list.append(list1[i])
    for i2 in range(len(list2)):
        new_list.append(list2[i2])
    return new_list


def sub(list_og: list[int], idx1: int, idx2: int) -> list[int]:
    """Generate sublist using two given indexes."""
    sub_list: list[int] = []
    LENGTH: int = len(list_og)
    if idx2 > LENGTH:
        idx2 = LENGTH
    idx2 -= 1
    if idx1 < 0:
        idx1 = 0
    if LENGTH == 0 or idx1 >= LENGTH or idx2 <= 0:
        return sub_list
    else:
        sub_list.append(list_og[idx1])
        sub_list.append(list_og[idx2])
    return sub_list