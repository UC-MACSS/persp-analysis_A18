primes = [2, 3, 5]
i = 6
while len(primes) < 10001:
	prime = True
	for num in range(2, i - 1):
		if i % num == 0:
			prime = False
	if prime:
		primes.append(i)
	i += 1

print(primes[10000])
