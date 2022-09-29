# This is a sample Python script.
import pydantic
from pydantic import BaseModel, constr


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class MyModel(BaseModel):
    MyField: constr(min_length=9, max_length=9)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m = MyModel(MyField = "123456789")
    print("hello")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
