# Todd Louison Makeup Exam

## Question 1

Collision attacks are prevalent and powerful against hashing algorithms that don't hash their input to enough bits to be computationally safe from the attack. They work based on the premise that hash functions contain a limited amount of possible hash values, and the likelihood that another unknown value must hash to the same value. The attack bases itself off of the birthday attack, which states that the probability of having a collision increases with every hash you do, so you likely only need 2<sup>n/2</sup> time to break a hash, where n is the bit length of the hash.

To perform the attack is realtively straight forward:

1. Intercept a message from a sender. For my code, I simply randomly generate a 32 bit number that acts as the intercepted message.
2. Hash it using the hash function that the message would have been hashed with.
3. Systematically test values from 0-(2<sup>31</sup>-1), checking each to see if it hashes to the same value.
4. When one is found to hash to the same value, you have broken the hash function.

In my implementation, I used Python3's built in hash-function, and modded it to hash to any length the user specifies. From this, I generate a random "intercepted" message, which I then use to break the hash function. From here I systematically check every value, checking each to find if they hash to the same value as the intercepted message. This can take a while, but it should finish in a relatively reasonable amount of time. I also decided to not allow the original message to be used when checking to see the other possible values, as this way allows me to prove that numbers other than the original input can hash to the desired value.

## Question 2

### 10-12

Consider the elliptic curve E7(2,1); that is, the curve is defined by y<sup>2</sup> = x<sup>3</sup>+2x+1
with a modulus of p = 7 . Determine all of the points in E<sub>7</sub>(2, 1)

| x    | y^2  | y1,y2 | p(x,y) | p'(x,y) |
| ---- | ---- | ----- | ------ | ------- |
| 0    | 1    | 1,6   | (0,1)  | (0,6)   |
| 1    | 4    | 2,5   | (1,2)  | (1,5)   |
| 2    | 6    | -     | -      | -       |
| 3    | 6    | -     | -      | -       |
| 4    | 4    | 2,5   | (4,2)  | (4,5)   |
| 5    | 3    | -     | -      | -       |
| 6    | 4    | -     | -      | -       |



**Answer: (0,1); (0,6); (1,2); (1,5); (4,2); (4,5)**

### 10-13

What are the negatives of the following elliptic curve points over Z7? P = (3, 5);
Q = (2, 5); R = (5, 0).

To find the negative of a point, you use the formula

$P=(x_p, y_p)$

$-P = (x_P, -y_P \text{ mod p})$

where p is the prime. Using this, we can find the negatives.

**Answer: -P = (3,2); -Q = (2,2); -R = (5,0)**

### 10-14

For E11(1, 7), consider the point G = (3, 2). Compute the multiple of G from 2G
through 13G.

Each of these values are determined using the addition law for ECC.

**G = (3,2)**

------

2G = 1G + 1G = (3,2) + (3,2)

​	m = $(3(3^2) + 1 )/ 2(2)$ mod 11 = 7 mod 11 = 7

​	$x_3 = (7^2 - 3 - 3)$mod 11 = 10

​	$y_3 = 7(3-10)-2$ mod 11 = 4

**2G = (10,4)**

------

3G =  2G + 1G = (10,4) + (3,2)

​	m = (2-4)/(3-10) mod 11 = 2 * $7^{-1}$ mod 11 = 2*8 mod 11 = 5

​	$x_3 = 5^2 - 10 - 3$ mod 11 = 1

​	$y_3 = 5(10-1) - 4 $ mod 11 = 8

**3G = (1,8)**

------

From here on out, I will just list what multiple I am calculating, which values I am adding to get it, and what the result it.

**4G = 2G + 2G = (10,4) + (10,4) = (5,4)**

**5G = 3G + 2G = (1,8) + (10,4) = (4,8)**

**6G = 3G + 3G = (1,8) + (1,8) = (7,7)**

**7G = 4G + 3G = (5,4) + (1,8) = (6,8)**

**8G = 4G + 4G = (5,4) + (5,4) = (10,3)**

**9G = 5G + 4G = (4,8) + (5,4) = (7,4)**

**10G = 5G + 5G = (4,8) + (4,8) = (4,3)**

**11G = 6G + 5G = (7,7) + (4,8) = (5,7)**

**12G = 6G + 6G = (7,7) + (7,7) = (1,3)**

**13G = 7G + 6G = (6,8) + (7,7) = (9,6)**

### 10-15

This problem performs elliptic curve encryption/decryption using the scheme outlined in Section 10.4. The cryptosystem parameters are E11(1, 7) and G = (3, 2). B’s private key is nB = 7.

#### a. Find B’s public key PB.

$P_B = n_B * G = 7*(3,2) = 7P = (6,8)$

#### b. A wishes to encrypt the message Pm = (10, 7) and chooses the random value k = 5. Determine the ciphertext Cm.
$C_m = \{kG, P_m + kP_B\} = \{5(3,2), (10,7)+5(6,8)\}$

We must now find what $5*(6,8)$ is. Using the methods performed in part 10-14 with the Law of Addition for ECC, we can find that $5*(6,8) = (7,10)$. We know $5*(3,2)$ from 10-14. 

We know know that:

$C_m = \{5(3,2), (10,7)+5(6,8)\} = \{(4,8), (10,7) + (7,10)\}$

We now add (10,7) and (7,10) to get a value of (6,0). Therefore:

$C_m = \{(4,8), (6,0)\}$

#### c. Show the calculation by which B recovers Pm from Cm.

There is an error somewhere in my calculations that cause me to always end up dividing by 0 which causes me to have to stop at that point. If you were to do this calculation however, this is how you would do it:

​							We use the formula 

​						$P_m + kP_B - n_B(kG) = P_m$				

- Then, calculate $n_B(kG)$.
- Flip the value of this point, as it is negative in the equation.
  - Flip the value using the negation formula for points
  - -P = (x<sub>P</sub>, -y<sub>P</sub> mod p)
- Now, add the flipped value to the original $P_m + kP_B​$ which we know from part b. Once these are added, you will have your plaintext back.



## Question 3

The results of primality for the 4 numbers is this:

- Prime: 31531,  485827, 15485863
- Composite: 520482 (trivially, as it can be divided by 2)

These prime numbers all passed the Miller-Rabin algorithm implemented in my code, however they do take a good while to process. Depending on hardware, the program could take anywhere from 15 minutes to a few hours to compute them all.

Since 520482 is composite, we perform Pollard's Rho method to find the first factor. The first factor we find is 3, which means that at least 1, 3, 173494, and 520482 are factors of 520482.