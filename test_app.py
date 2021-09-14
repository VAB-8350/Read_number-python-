from function import formulate, grouper
from read_number import read_number

def test_formulate():
    assert formulate('123 ') == '321'

def test_grouper():
    assert grouper(3, '123234') == ['123', '234']

def test_read_mumber():
    assert read_number('123234') == 'ciento veintitres mil doscientos treinta y cuatro'