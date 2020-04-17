import os
import sys


def print_interpreter():
    print(sys.implementation)


def main():
    print('program successfully initiated')
    return os.getcwd()


if __name__ == '__main__':
    print_interpreter()
    main()
