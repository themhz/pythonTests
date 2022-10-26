def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes


listOfAllPrimes = prime_numbers(100)

def getprimefactors(n):
    primefactors = []
    primeind = 0
    p = listOfAllPrimes[primeind]
    while p <= n:
        if n % p == 0:
            primefactors.append(p)
            n //= p
        else:
            primeind += 1
            p = listOfAllPrimes[primeind]
    return primefactors

result = getprimefactors(24)

for i in range(len(result)):
    if(i==0):
        d = result[i]
    else:
        if(result[i-1] == result[i])
            d=d+result[i]
