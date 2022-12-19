# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from data import contacts

jenny_email = contacts["Jenny"]["email"]

def my_function(n1,n2):
    total = n1 + n2
    return total

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(my_function(1,2))
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
