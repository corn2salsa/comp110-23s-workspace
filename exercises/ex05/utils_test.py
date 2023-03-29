"""Unit tests."""
from exercises.ex05.utils import only_evens, sub, concat
__author__: "730614170"


def test_evens_only_odds() -> None:
    """List is only odd."""
    odd_list: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(odd_list) == []


def test_evens_works() -> None:
    """Does only_evens work?"""
    working_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(working_list) == [2, 4, 6]


def test_working_even() -> None:
    """Double checking."""
    list_works: list[int] = [1, 1, 1, 1, 1, 1, 8, 1]
    assert only_evens(list_works) == [8]


def test_concat_empty_list() -> None:
    """Works is one list is empty."""
    list_full: list[int] = [1, 2, 3, 1]
    list_empty: list[int] = []
    assert concat(list_full, list_empty) == [1, 2, 3, 1]


def test_concat_specific() -> None:
    """Specific concat test."""
    list1: list[int] = [1, 2, 3, 1]
    list2: list[int] = [8, 9, 14, 6]
    assert concat(list1, list2) == [1, 2, 3, 1, 8, 9, 14, 6]


def test_concat_test() -> None:
    """Specific concat 2."""
    list1: list[int] = [9000000, 800000, 1]
    list2: list[int] = [4, 4, 4, 4, 4]
    assert concat(list1, list2) == [9000000, 800000, 1, 4, 4, 4, 4, 4]


def test_sub_works() -> None:
    """Does sub work?"""
    test_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sub(test_list, 4, 8) == [4, 7]


def test_sub_empty() -> None:
    """OG list is empty."""
    empty_list: list[int] = []
    assert sub(empty_list, 1, 3) == []


def test_sub_specific() -> None:
    """Testing to see if Sub works."""
    test_list: list[int] = [7, 9, 46, 9092]
    idx1: int = 1
    idx2: int = 3
    assert sub(test_list, idx1, idx2) == [9, 46]
