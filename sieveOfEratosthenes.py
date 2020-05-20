# Function to generate prime numbers till a given number
# Returns a list of the generated prime numbers


def sieve(number):

    # create a list of length n-1 that starts from number 2 to n-1
    primeList = [True] * (number - 1)

    # set p initial to 2
    prime = 2

    # run a loop to cross off multiples of p
    while True:
        increment = 2
        multiple = prime * increment

        # loop to cross off Values
        while multiple <= number:
            primeList[multiple - 2] = False
            increment = increment + 1
            multiple = prime * increment

        # Finding New P
        newPrime = calcPrime(primeList, prime)
        if newPrime == prime:
            break
        else:
            prime = newPrime

    # printing Primes and generating final list
    onlyPrimes = []
    # print("List of Primes")
    for index, value in enumerate(primeList):
        if value == True:
            # print(index + 2)
            onlyPrimes.append(index + 2)

    print(onlyPrimes)
    print(len(onlyPrimes))


# Function to calculate P
def calcPrime(primeList, prime):
    for index, value in enumerate(primeList):
        if value == True and index + 2 > prime:
            prime = index + 2
            return prime
    return prime


def calcSpecificPrime(number):
    initial = 20000
    listOfPrimes = sieve(initial)
    while len(listOfPrimes) < number:
        initial = initial * 2
        listOfPrimes = sieve(initial)

    print(listOfPrimes[number - 1])


# calcSpecificPrime(10001)
sieve(100)
