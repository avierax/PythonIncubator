# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def make_counter():
    l = 0
    def counter():
        nonlocal l
        l = l + 1
        return l
    return counter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    c = make_counter()
    print(c())
    print(c())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
