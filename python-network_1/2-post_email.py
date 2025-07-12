#!/usr/bin/python3
"""POST an email"""
from urllib import parse, request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, email)
    req.add_header("cfclearance", "true")

    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
