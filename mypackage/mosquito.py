from beautiful_date import D

def display_dates():
    print("Enter 1 if date today")
    print("Enter 2 if date tomorrow")
    print("Enter 3 if date yesterday")
    print("Enter 4 if exit")

def date_function():
    date_now = D.today()
    next_day = D.tomorrow()
    last_day = D.yesterday()

    while True:
        display_dates()
        
        choice = input("Enter your choice: ")

        dmy_format_today = f"{date_now.day}/{date_now.month}/{date_now.year}"
        dmy_format_tomorrow = f"{next_day.day}/{next_day.month}/{next_day.year}"
        dmy_format_yesterday = f"{last_day.day}/{last_day.month}/{last_day.year}"
        
        if choice == "1":
            print("\n")
            print(f"This is the date today: {dmy_format_today}\n")   
        elif choice == "2":
            print("\n")
            print(f"This is the date tomorrow: {dmy_format_tomorrow}\n")
        elif choice == "3":
            print("\n")
            print(f"This is the date yesterday: {dmy_format_yesterday}\n")
        elif choice == "4":
            print("Exiting....")
            break
        else:
            print("Choice is invalid!!!")