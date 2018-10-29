'''
Makeup Exam Problem 3 Implementation
By: Todd Louison
'''
import random
import numpy
from decimal import Decimal

'''
This takes in a value and performs a process to gather what the number is in the form
(2**n) * d, and returns the d value.
'''
def getSAndD(val):
    s = 1
    while s < val-1:
        d = (val-1) / (2**s)

        #If d < 1, then there is no chance of the number being decomposed correctly
        if (d < 1):
            break

        #If we found a d that is odd and an integer, we have found the d that works
        if ((d % 2) == 1):
            return (int(s),int(d))
        #Otherwise, we increment up by 1 and try again.
        s += 1
    #Error case
    return (-1, -1)

'''
Takes in an int and uses the Miller-Rabin primality test to determine if the value
is either composite, or if it is likely prime. This test is not flawless due to the
existence of Carmichael Numbers, which are composites that pass the primality test.
It also takes an acc value, which is the accuracy value. This determines how many times
the test will be run.
'''
def primeTester(val, acc):
    (s, d) = getSAndD(val)
    if (d == -1):
        return "composite"

    if val <= 3:
        return "an error. Value must be greater than 3"

    #Run as many times as the accuracy value determines
    trials = 0
    while trials < acc:
        #This trial has not effectively determined the number is not prime
        inconclusive = False
        #Generating a random base value to raise the the d power
        randomBase = numpy.random.randint(2, val-1)

        numer = randomBase**d
        x = numpy.mod(numer, val)

        if x == 1 or x == (val - 1):
            inconclusive = True

        #Check to see if the number can be determined composite by repeated squaring
        for j in range(s-1):
            x = numpy.mod( numpy.power(x,2), val)
                   
            if x == (val-1):
                inconclusive = True
                break

        #If the previous loop left the val still undetermined, run the loop again
        if inconclusive:
            trials += 1
            continue

        return "composite"
    return "probably prime"

'''
Euclid's Algorithm for finding the GCD of two values
'''
def gcd(x, y):
    while x % y != 0:
        temp_y = y
        y = x%y
        x = temp_y
    return y

'''
Implements the Pollard Rho Algorithm in order to 
factor a non-prime number into its composite values
'''
def pollardRho(val):
    x = 2
    fixedX = 2
    size = 2
    foundFactor = 1

    while foundFactor == 1:
        count = 1

        while count <= size and foundFactor <= 1:
            x_numer = (x*x)+1
            x = x_numer % val

            foundFactor = gcd(x - fixedX, val)

            count += 1

        size *= 2
        fixedX = x

    return foundFactor



# Primes: 31531; 485827; 15485863
# Composite: 520482;
if __name__ == "__main__":
    numbers = [31531, 520482, 485827, 15485863]
    accuracy = 50

    choice = int(input("Would you like to prime test(1) or factor the composite(2)? "))
    #If they want to determine primes, run the primeTester function to determine which, if any
    #of the given numbers are prime.
    if choice == 1:
        for num in numbers:
            PorC = primeTester(num, accuracy)
            print("\n{:} is {:}.".format(num, PorC))

    #Run Pollard's Rho algorithm to find the first factor of the composite number we found
    #Composite is hardcoded, but was found using the prime tester. Only done this way due
    #to the length of computation in the primeTester function.
    else:
        factor = pollardRho(520482)
        print("The first factor of {:}  is {:}".format(520482, factor))