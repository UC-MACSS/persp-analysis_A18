<<<<<<< HEAD
import numpy as np
def get_r(K, L, alpha, Z, delta):
	'''
	This function generates the interest rate or the vector of interest rates
	'''
	r = (alpha * Z * np.power(L / K, 1 - alpha)) - delta
	return r
=======
'''
------------------------------------------------------------------------
This module contains the function get_r()
------------------------------------------------------------------------
'''


def get_r(K, L, alpha, Z):
    r = alpha + Z * (L / K) ** alpha

    return r
>>>>>>> 85363c57b96194e82483e246e982d59653920437
