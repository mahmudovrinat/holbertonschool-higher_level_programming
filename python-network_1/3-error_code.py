#!/usr/bin/python3
""" Send a request and handle exception"""
import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    req.add_header("cfclearance", 'true')

    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code:", e.code)
