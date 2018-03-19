#Function to generate prime numbers till a given number
#Returns a list of the generated prime numbers

def sieve(number):

	#create a list of length n-1
	primeList = [True]*(number-1)

	#set p initial to 2
	p = 2

	#run a loop to cross off multiples of p
	while True:
		increment = 2
		multiple = p*increment

		#loop to cross off Values
		while multiple <= number:
			primeList[multiple-2] = False
			increment = increment + 1
			multiple = p*increment


		#Finding New P			
		newP = calcP(primeList, p)
		if newP == p:
			break
		else:
			p = newP


	#printing Primes and generating final list
	onlyPrimes = []
	print("List of Primes")
	for index, value in enumerate(primeList):
		if value == True:
			print(index+2)
			onlyPrimes.append(index+2)

	return onlyPrimes


#Function to calculate P
def calcP(primeList, p):
	for index, value in enumerate(primeList):
		if value == True and index+2 >p:
			p = index+2
			return p
	return p			