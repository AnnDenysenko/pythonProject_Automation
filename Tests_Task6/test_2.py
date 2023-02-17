from request import single_request

URL = "https://ovokogroup.com/"


def test_first_total_seconds():
    actual_result = single_request(URL).elapsed.total_seconds()
    assert actual_result < 2


def test_fistory_status_code():
    actual_results = single_request(URL).history
    for actual_result in actual_results:
        assert actual_result.status_code == 301


def test_content_type():
    actual_results = single_request(URL).headers.get("Content-Type")
    assert actual_results == "text/html; charset=UTF-8"
