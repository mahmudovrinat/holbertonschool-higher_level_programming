#!/usr/bin/python3
for c in range(97, 123):
    if c not in (101, 113):  # 101='e', 113='q'
        print("{}".format(chr(c)), end="")
