'''
Assignment 7
Author: Sanittawan Tan 
'''
def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate or vector of interest rates
    '''
    r = (alpha * Z * ((L / K) ** (1 - alpha))) - delta

    return r
