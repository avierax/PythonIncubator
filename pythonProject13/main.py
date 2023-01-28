# This is a sample Python script.
import os
import re
from pathlib import Path
from pprint import pprint


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def contains_tag(lines):
    return next((True for x in lines if x.__contains__("#journal") or x.__contains__("#Journal")), False)


def find_best_place_to_put_tag(lines):
    return 1


def tag(file):
    file_open = file.open()
    lines = file_open.readlines()
    file_open.close()
    if not contains_tag(lines):
        pprint(f"does not contains tag {file}")
        place = find_best_place_to_put_tag(lines)
        lines.insert(place, "#journal")
        print(f"tagging {file}")
        file.open("w").writelines(lines)


def is_candidate_for_tag(r):
    if r.absolute().__str__().__contains__("journal"):
        if re.match(r"\d\d\d\d-\d\d-\d\d.md", r.name):
            return True
    return False


if __name__ == '__main__':
    print(os.getcwd())
    result = Path(".").rglob("*.md")
    for r in result:
        print(f"checking {r}",)
        if is_candidate_for_tag(r):
            print(f"...candidate")
            tag(r)
        else:
            print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
