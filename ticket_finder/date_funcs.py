import datetime

def create_date_list(date_1,date_2):
    new_date = date_1
    dates = []
    while new_date <= date_2:
        dates.append(date_to_str(new_date))
        new_date = str_to_date(dates[-1]) + datetime.timedelta(days=1)
    return dates

    
def date_to_str(date):
    return str(date.year)+"-" + str(date.month) + "-" +str(date.day)


def str_to_date(string):
    return datetime.datetime(int(string.split("-")[0]),int(string.split("-")[1]),int(string.split("-")[2]))