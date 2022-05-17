from bs4 import BeautifulSoup
import  requests 


def make_url(origin,destination,date,international,adult=1,child=0,infant=0):
    flight_type = None
    if international:
        flight_type = "international"
    else:
        flight_type = "flights"
    search_url = "https://www.alibaba.ir/{}/{}-{}?adult={}&child={}&infant={}&departing={}".format(
        flight_type,origin,destination,adult,child,infant,date
    )
    return search_url


def get_content(content_url):
    pass


def search_price():
    pass
