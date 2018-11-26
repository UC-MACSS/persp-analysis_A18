import pytest

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
    for i in range(2, int(n**.5) + 1):
        if n % i == 0: return i
    return n

def test_factor():
	# previous case failed because the root of a number between 2 and 3 will reuslt in no range
	assert smallest_factor(25) == 5
	# also  int means that it always rounds down
	assert smallest_factor(4) == 2
	# following tests are for full coverage
	assert smallest_factor(1) == 1
	assert smallest_factor(7) == 7