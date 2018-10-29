import random
import time

def findCollision(message):
    #Define the hash function for m1 and get it's hash value
    originalHash = hash(message) % (2**HASH_LENGTH)
    noCollision = True

    message2 = -1
    while noCollision:
        #Choose a message, with another value from 0 to 2^31-1 then hash it to 16 bits to conduct a 16-bit hash birthday attack
        message2 += 1 
        messageHash = hash(message2) % (2**HASH_LENGTH)

        if originalHash == messageHash and message != message2:
            noCollision = False
            print("Collision found! The messages {:} and {:} produce the same hash value of {:}.".format(bin(message)[2:], bin(message2)[2:], messageHash))
            break

if __name__ == "__main__":
    global HASH_LENGTH
    HASH_LENGTH = input("How long would you like the hash length to be? The larger the value, the longer this will take.\n => ")
    print("Generating a random number...")
    time.sleep(1)
    #The message that was "stolen", and we are trying to find an identical hash to
    stolenText = random.randint(0,2147483647)
    print("Finding collision...")
    findCollision(stolenText)