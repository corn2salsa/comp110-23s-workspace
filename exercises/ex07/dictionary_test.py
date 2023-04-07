"""Dictionary Utils unit tests."""
from exercises.ex07.dictionary import invert, favorite_colors, count
import pytest
__author__: "730614170"

def test_invert_works() -> None:
    """Dict is properly inverted."""
    invert_dict: dict[str,str] = {'Obama': 'Barack'}
    assert invert(invert_dict) == {'Barack': 'Obama'}


def test_invert_2() -> None:
    """Dict is properly inverted 2."""
    invert_dict: dict[str,str] = {'Lebron': 'James', 'Michael': 'Jordan'}
    assert invert(invert_dict) == {'James': 'Lebron', 'Jordan': 'Michael'}


with pytest.raises(KeyError):
    """Same key error."""
    edge: dict[str,str] = {'Zach': 'Wachtel', 'Maddie': 'Wachtel'}
    invert(edge)


def test_count_use() -> None:
    """"""
    use: list[str] = ["blue", "blue", "red", "orange"]
    assert count(use) == {'blue': 2, 'red': 1, 'orange': 1}


def test_count() -> None:
    use: list[str] = ["batman", "Batman", "batMan", "Batman", "batman", "batman", "batman"]
    assert count(use) == {'batman': 4, 'Batman': 2, 'batMan': 1}


def test_count_edge() -> None:
    edge: list[str] = []
    assert count(edge) == {}


def test_favorite_colors():
    """Works properly."""
    use: dict[str,str] = {'zach': 'purple', 'liz': 'purple'}
    assert favorite_colors(use) == "purple"


def test_favorite_colors_2():
    """Works properly."""
    use: dict[str,str] = {'zach': 'purple', 'liz': 'purple', 'jordan': 'red', 'mac': 'blue'}
    assert favorite_colors(use) == "purple"


def test_favorite_colors_edge():
    """Works properly."""
    edge: dict[str,str] = {'zach': 'purple', 'liz': 'purple', 'jordan': 'red', 'mac': 'red'}
    assert favorite_colors(edge) == "purple"