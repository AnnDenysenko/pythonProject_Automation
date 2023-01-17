

import requests



def first_request(url):
    r = requests.get(url)
    return r.status_code

def test_first_request():
    url = 'https://www.delfi.lt'

    actual_result = first_request(url)

    assert actual_result == 200