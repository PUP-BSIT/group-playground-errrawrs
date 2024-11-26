from datetime import date
from beautiful_date import D

def date_function():
    date_now = date.today()
    next_day = D.tomorrow()
    last_day = D.yesterday()

    print("Enter 1 if date today")
    print("Enter 2 if date tomorrow")
    print("Enter 3 if date yesterday")
    print("Enter 4 if exit")

    while True:

        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("This is the date today:",date_now)   
        elif choice == "2":
            print("This is the date tomorrow:",next_day)
        elif choice == "3":
            print("This is the date yesterday:", last_day)
        elif choice == "4":
            print("Exiting this module")
            break
        else:
            print("Choice is invalid!!!")