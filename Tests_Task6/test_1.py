from request import single_request

URL = "https://www.rrr.lt/"


def test_first_status_code():
    actual_result = single_request(URL).status_code
    assert actual_result == 200


def test_second_request_url():
    actual_result = single_request(URL).request.url
    assert actual_result == URL.replace("www.", "")


def test_third_line_in_text():
    actual_result = single_request(URL).text
    assert "Naudotos automobilių dalys internetu" in actual_result
