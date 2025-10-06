from lib.report_length import *

def test_report_length():
    result = report_length("Anna")
    assert result == "This string was 4 characters long."