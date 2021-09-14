from function import formulate, grouper

def test_answer():
    assert formulate('123 ') == '321'
    assert grouper(3, '123234') == ['123', '234']