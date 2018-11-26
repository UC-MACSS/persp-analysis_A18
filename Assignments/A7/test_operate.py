import pytest

def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")

def test_operate():

    with pytest.raises(TypeError) as execinfo: 
        operate(1, 3, 3)
    assert execinfo.value.args[0] == "oper must be a string"
    
    with pytest.raises(ZeroDivisionError) as execinfo:
        operate(1, 0, '/')
    assert execinfo.value.args[0] == "division by zero is undefined"

    with pytest.raises(ValueError) as execinfo: 
        operate(1, 3, 'hi')
    assert execinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

    assert operate(1, 1, '+') == 2
    assert operate(1, 1, '-') == 0
    assert operate(1, 1, '*') == 1
    assert operate(1, 1, '/') == 1