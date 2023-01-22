# This is a sample Python script.
import random
from pprint import pprint

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = list(random.random(0, 2) for i in range(0, 10))
    pprint(numbers)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
