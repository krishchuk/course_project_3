from utils.functions import sort_by_state, sort_by_date, date_format, encoding_number


def test_sort_by_state():
    operations = sort_by_state()
    for operation in operations:
        assert "EXECUTED" in operation["state"]
        assert "CANCELED" not in operation["state"]


def test_sort_by_date():
    operations = sort_by_date()
    for i in range(len(operations) - 1):
        assert operations[i]["date"] > operations[i + 1]["date"]
        i += 1


def test_date_format():
    assert date_format("2018-09-12T21:27:25.241689") == "12.09.2018"
    assert date_format("2019-04-14T19:35:28.978265") == "14.04.2019"
    assert date_format("2020-10-15T22:27:25.205631") == "15.10.2020"
    assert date_format("2022-08-24T25:17:25.205631") == "24.08.2022"
    assert date_format("1995-12-30T10:20:25.205631") == "30.12.1995"


def test_encoding_number():
    assert encoding_number("Счет 78808375133947439319") == "Счет **9319"
    assert encoding_number("Visa Classic 4195191172583802") == "Visa Classic 4195 19** **** 3802"
    assert encoding_number("Visa Gold 7305799447374042") == "Visa Gold 7305 79** **** 4042"
    assert encoding_number("Visa Platinum 2256483756542539") == "Visa Platinum 2256 48** **** 2539"
    assert encoding_number("MasterCard 4047671689373225") == "MasterCard 4047 67** **** 3225"
    assert encoding_number("Maestro 3806652527413662") == "Maestro 3806 65** **** 3662"
    assert encoding_number("МИР 8201420097886664") == "МИР 8201 42** **** 6664"
