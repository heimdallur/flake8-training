"""THIS IS AN EXAMPLE IS FREE OF LINTING ERROR"""

import os


def print_working_dir():
    print(os.getcwd())  # Returns the current working directory of the process


def print_something_n_times(n):
    for i in range(n):  # Will repeat the content n times
        print('Something')


if __name__ == '__main__':
    print_working_dir()
    print_something_n_times(3)
