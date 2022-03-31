#!/usr/bin/python3
# coding=utf-8
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__bar)


if __name__ == "__main__":
    main()
