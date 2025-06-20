#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div  # YALNIZ BİR DƏFƏ calculator_1 istifadə olunur

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
