from ticket_finder.search_engine import *



def disp_menu():
    print("""
1. Search Between Two Dates
2. Notify Me If an Specific Price is available
3. Exit
""")
    choice = input("Enter Your Choice:")
    try:
        if int(choice) == 1:
            pass
        elif int(choice) == 2:
            pass
        elif int(choice) == 3:
            pass
        else:
            raise Exception("Wrong Choice")
    except:
        print("wrong choice. please try again!")
        disp_menu()