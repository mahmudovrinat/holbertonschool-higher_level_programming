#!/usr/bin/python3
""" Python script that fetches """
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
