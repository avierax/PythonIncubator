import zoneinfo
from pprint import pprint
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def call1():
    raise 1

def call2():
    call1()

def call3():
    call2()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call3()
    print_hi('PyCharm')
    time_zones = zoneinfo.available_timezones()
    for key in time_zones:
        pprint(key)
        zoneInfo = zoneinfo.ZoneInfo(key)
        pprint(zoneInfo)


    new_york = zoneinfo.ZoneInfo("America/New_York")
    us_eastern = zoneinfo.ZoneInfo("US/Eastern")

    if new_york == us_eastern:
        print("they are equal")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
