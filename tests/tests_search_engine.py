import pytest
from ticket_finder.search_engine import *


def test_make_url():
    assert make_url("TBZ","ECN","1401-03-10",True) == "https://www.alibaba.ir/international/TBZ-ECN?adult=1&child=0&infant=0&departing=1401-03-10"


def test_get_content():
    pass


def test_search_price():
    pass