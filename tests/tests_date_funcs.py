from ticket_finder.date_funcs import *
import pytest

def test_create_date_list():
    assert create_date_list(datetime.datetime(1401,2,2),datetime.datetime(1401,2,4)) == ["1401-2-2","1401-2-3","1401-2-4"]


def test_str_to_date():
    assert str_to_date("1401-2-2")== datetime.datetime(1401,2,2)


def test_date_to_str():
    assert date_to_str(datetime.datetime(1401,2,2))== "1401-2-2"

def convert_date():
    pass