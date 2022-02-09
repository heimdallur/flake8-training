import datetime


def print_time():  # Will print the current time at execution

    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':

    print_time()
