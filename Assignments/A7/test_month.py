'''
Assignment 7
Author: Sanittawan Tan 
'''
import month

def test_month_length1():
    '''
    Test suit for month_length function
    '''
    assert month.month_length('September') == 30, "Wrong output. Should be 30"
    
def test_month_length2():
    '''
    Test suit for month_length function
    '''
    assert month.month_length('May') == 31, "Wrong output. Should be 31"
    
def test_month_length3():
    '''
    Test suit for month_length function
    '''
    assert month.month_length('February') == 28, "Wrong output. Should be 28"
    
def test_month_length4():
    '''
    Test suit for month_length function
    '''
    assert month.month_length('February', leap_year=True) == 29, "Wrong output. Should be 29"
    
def test_month_length5():
    '''
    Test suit when inputting an invalid string
    '''
    assert month.month_length('Foobar') == None, "Wrong input and output. \
            Should be None"