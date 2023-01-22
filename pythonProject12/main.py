# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class CacheTest:

    def return_foo(self):
        return [1]

    def result_something(self)-> bool:
        return self.return_foo()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    c = CacheTest()
    if c.result_something():
        print("asdf")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
