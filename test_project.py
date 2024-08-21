import pytest
from project import check_list
from project import out
from project import maximum_out

grocery_list = {}
total_price = 0

def test_check_list():
    list_0 = {}
    assert check_list(list_0) == None

def test_out():
    assert out(grocery_list) == ({}, 0)


def test_maximum_out():
    assert maximum_out() == print("The list has maximum 10 items.\n""Checking out...\n\n")


if __name__ == "__main__":
    main()
