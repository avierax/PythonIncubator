# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def merge_sort(numberlist: list[int]):
    if len(numberlist == 1):
        return numberlist
    # Use a breakpoint in the code line below to debug your script.
    middle = len(numberlist) // 2
    left = numberlist[:middle]
    print(left)
    right = numberlist[middle:]
    print(right)
    left = merge_sort(left)
    right = merge_sort(right)
    raise Exception("not implemented")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    random.seed(150)
    numbers: list[int] = list(random.randrange(0, 30) for i in range(0, 10))
    merge_sort(numbers)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
