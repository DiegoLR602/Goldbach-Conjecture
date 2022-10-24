'''
The Goldbach Conjecture is one that states that given an even number,
two prime numbers can be summed together to equal that even number. No proofs
exist that prove or disprove this claim, hence it's classification as a
conjecture. This program finds the two primes that add up to the user's
inputted values, demonstrating the conjecture's power.
'''

import math

def primechecker(prime): #Checks if a number is prime
    if (prime == 0 or prime == 1): #0 and 1 aren't prime by definition, rules them out
        return False
    for i in range(2,math.floor(math.sqrt(prime))+1): #Checks all factors of the number its checking
        if (prime/i)%1 == 0 and (prime/i) > 1: # Ensures the number its checking isn't divisible by any number except itself and 1
            return False #returns false if not prime
    return True #returns true if it passes the checks and is prime

def primegenerator(numprimes): #Generates a list of n prime numbers
    diffprimes = [] #initializes list to store primes
    counter = 0
    while len(diffprimes) < numprimes: #Keeps adding to the list until its length is the input
        if primechecker(counter): #calls primechecker() to test if the number counter is prime
            diffprimes.append(counter) #adds the number counter to the list if its prime
        counter += 1
    return diffprimes #Returns a list of prime numbers

def goldbach(evenint): #Tests if the Goldbach Conjectures is valid for that even int
    p1 = primegenerator(evenint) #Creates a list of primes that is evenint numbers long
    p2 = primegenerator(evenint)
    for prime1 in p1:
        for prime2 in p2: #Goes through every sum possible of the list of primes
            if prime1+prime2 == evenint: # Once a sum is found, it immediately returns them
                return (prime1,prime2)
    print ("Proof broken!") #If no sums are found and the conjecture is proved wrong, reports it

numba = int(input("Please enter an even number greater than two: "))
while numba%2 != 0 and numba > 2: #Keeps asking for inputs that are even and greater than 2
    numba= int(input("Please only enter an even int thats greater than two: "))

print(goldbach(numba))
