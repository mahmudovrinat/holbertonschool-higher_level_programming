#!/usr/bin/python3
""" Python script that fetches """
from urllib import request


if __name__ == "__main__":
    req = request.Request("https://intranet.hbtn.io/status ")
    req.add_header('cfclearance', 'true')

    with request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(utf8_content))
