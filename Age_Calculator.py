from datetime import date

print("\nWelcome to Age Calculator \n".center(90,'-'))

print("Please mention your birth date, month and year.")
day = int(input("Enter the date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

print("\nYour DOB is : {:02d}/{:02d}/{:4d}\n".format(day,month,year))

total_years = date.today().year - year
months = date.today().month - month
days = date.today().day - day

print("Your Age is: {:02d} years, {:02d} months and {:02d} days".format(total_years,months,days))

def units():

    unit = input("\nPlease choose the time unit: months or weeks or days or hours or minutes(mi) or seconds. \nNote: You can write the first letter or the full name of the time unit. \nEnter your option: ").lower()

    total_months = total_years * 12 + month
    week = total_months * 4
    total_days = total_years * 365 + month * 30 + day
    hours = total_days * 24
    minutes = hours * 60
    seconds = minutes * 60

    if unit == "months" or unit == "m":
        print(f"\nYou lived for {total_months:,} months\n")

    elif unit == "weeks" or unit == "w":
        print(f"\nYou lived for {week:,} weeks\n")

    elif unit == "days" or unit == "d":
        print(f"\nYou lived for {total_days:,} days\n")

    elif unit == "hours" or unit == "h":
        print(f"\nYou lived for {hours:,} hours\n")

    elif unit == "minutes" or unit == "mi":
        print(f"\nYou lived for {minutes:,} minutes\n")

    elif unit == "seconds" or unit == "s":
        print(f"\nYou lived for {seconds:,} seconds\n")

    else:
        print("\nPlease Enter a valid Character\n".center(94,'-'))

    def another_input():
        N = input("Do you want your age in another unit? \'Yes\' or \'No \': ").lower()
        return N

    def second_option():
        N = another_input()
        if N == "yes":
            units()
        elif N == "no":
            print("\nThank You!")
            exit()
        else:
            print("\nPlease Enter a Valid Character\n".center(94,'-'))
            second_option()

    second_option() # Calling second option function

def option():
    print("\nDo you want your age in months or weeks or days or hours or minutes or seconds?")
    Q = input("Please Enter \'Yes\' or \'No\': ").lower()

    if Q == "yes":
        units()
    elif Q == "no":
        print("\nThank You!")
        exit()
    else:
        print("\nPlease Enter a Valid Character\n".center(94,'-'))
        option()

option() # Calling option function