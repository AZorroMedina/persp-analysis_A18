# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:46:27 2018

@author: Angela
"""

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
    assert operate(1, 3,'+') == 4, "failed on positive integers"
    assert operate(-5, -7,'+') == -12, "failed on negative integers"
    assert operate(1, 3,'-') == -2, "failed on positive integers"
    assert operate(-5, -7,'-') == 2, "failed on negative integers"
    assert operate(3, 1,'-') == 2, "failed on positive integers"
    assert operate(-5, 7,'-') == -12, "failed on mixed integers"
    assert operate(1, 3,'*') == 3, "failed on positive integers"
    assert operate(-5, -7,'*') == 35, "failed on negative integers"
    assert operate(-5, 7,'*') == -35, "failed on mixed integers"
    assert operate(4,2,'/') == 2, "integer division"
    assert operate(5,4,'/') == 1.25, "float division"
    pytest.raises(ZeroDivisionError, operate, a=4, b=0,'/')