import requests


def single_request(url):
    r = requests.get(url)
    return r
