#!/usr/bin/python3
""" Python script that fetches """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    print(response.headers.get("X-Request-Id"))
