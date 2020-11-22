import math

def getLowestPrimeFactor(num, start):
    start = int(min(num, max(3, start)))
    root = math.floor(math.sqrt(num))

    if num % 2 == 0:
        return 2

    for i in range(start, root + 1, 2):
        if num % i == 0:
            return int(i)
    return int(num)

def getPrimeFactors(num):
    factorList = []
    factor = 2

    while num > 1:
        factor = getLowestPrimeFactor(num, factor)
        factorList.append(factor)
        num /= factor

    if len(factorList) == 0:
        factorList.append(num)

    return factorList

def getLargestPrimeFactor(num):
    factors = getPrimeFactors(num)
    return factors[len(factors) - 1]

print(getLargestPrimeFactor(600851475143))
