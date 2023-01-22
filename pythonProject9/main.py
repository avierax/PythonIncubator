# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Base:
    def foo(self):
        return "basefoo"

    def bar(self):
        return f"{self.foo()} and bar"


class Mixin(Base):
    def foo(self):
        return "mixingfoo"


class Derived(Base, Mixin):
    pass

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(Derived().bar())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
