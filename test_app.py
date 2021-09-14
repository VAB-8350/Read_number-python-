from function import formulate, grouper
from read_number import read_number

def test_answer():
    assert formulate('123 ') == '321'
    assert grouper(3, '123234') == ['123', '234']
    assert read_number('123234') == 'ciento veintitres mil doscientos treinta y cuatro'