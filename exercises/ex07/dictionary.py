"""Dictionary Utilities."""
__author__: "730614170"


def invert(og_dict: dict[str,str]) -> dict[str,str]:
    """Invert dictionary."""
    error_list: list = []
    error_list = list(og_dict.values())
    i: int = 0
    idx: int = 1
    for i in range(0,len(error_list) + 1):
        if error_list[i] == error_list[idx]:
            raise KeyError("idiot.")
        idx += 1
    sub_dict: dict[str,str] = {}
    for key, value in og_dict.items():
        sub_dict[value] = key
    return sub_dict


def favorite_colors(colors: dict[str,str]) -> str:
    """Returns most frequent color."""
    color: str = ""
    idx: int = 0
    i: int = 1
    color_list: list
    color_dict: dict[str,int] = {}
    color_list = list(colors.values())
    print(color_list)
    color_dict = count(color_list)
    print(color_dict)
    playing: bool = True
    length = len(color_list)
    for idx in range(0, length):
        while playing == True and len(color_dict) != 1:
            if color_dict[color_list[idx]] >= color_dict[color_list[i]]:
                color_dict.pop(color_list[i])
                i += 1
            else:
                color_dict.pop(color_list[idx])
                print(color_dict)
                i = 1
                playing = False
        playing = True
    color = str(list(color_dict))
    return color


def count(og_list: list[str]) -> dict[str,int]:
    """Adding keys, and enumerating values."""
    new_dict: dict[str,int] = {}
    idx: int = 0
    while idx < len(og_list):
        if og_list[idx] in new_dict:
            new_dict[og_list[idx]] += 1
            idx = idx + 1
        else:
            new_dict.update({og_list[idx]: 1})
            idx = idx + 1
    return new_dict
