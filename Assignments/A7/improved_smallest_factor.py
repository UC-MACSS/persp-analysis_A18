'''
Assignment 7
Author: Sanittawan Tan 
'''
def improved_smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if not n or (n <= 0) or (n == 1) or (type(n) == float):
        return None
    for i in range(2, int(n**.5) + 1):
        print('for executed', i)
        if n % i == 0:
            print(n, i)
            return i
    return n
