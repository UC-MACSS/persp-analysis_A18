import numpy as np
def get_r(K, L, alpha, Z, delta):
	'''
	This function generates the interest rate or the vector of interest rates
	'''
	r = (alpha * Z * np.power(L / K, 1 - alpha)) - delta
	return r
