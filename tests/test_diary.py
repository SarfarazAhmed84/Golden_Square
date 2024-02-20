from lib.diary import *

def test_empty_diary():
    result = make_snippet('test')
    assert len(result) > 0

def test_last_three_chars():
    result = make_snippet('test12345')
    assert len(result) >= 3 and result[-3:] == '...'

def test_total_number_of_chars_is_eight():
    #function should only produce first 5 characters of the string plus '...' therefore 8 characters in total
    result = make_snippet('123456789')
    assert len(result) == 8