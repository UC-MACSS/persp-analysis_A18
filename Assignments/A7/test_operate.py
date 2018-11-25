'''
Assignment 7
Author: Sanittawan Tan 
'''
import operate as op
import pytest

def test_operate():
    '''
    Test suite for operate function
    '''
    with pytest.raises(TypeError) as excinfo:
        op.operate(3, 4, 3.14)
    assert excinfo.value.args[0] == "oper must be a string"
    assert op.operate(2, 3, '+') == 5, "Wrong output"
    assert op.operate(20, 0, '-') == 20, "Wrong output"
    assert op.operate(15, 1, '*') == 15, "Wrong output"
    assert op.operate(9, 3, '/') == 3, "Wrong output"
    with pytest.raises(ZeroDivisionError) as excinfo:
        op.operate(20, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        op.operate(20, 0, 'foo')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
