#Program to demo the RSA encryption algorithm with a user supplied message.
#07/23/2023
#Ha.Ha.
from math import gcd
import random
#Test for a random number between 6 and 100, recursively calls itself until tested number is prime, at wich point the prime is returned.
def returnRandPrime():
	test = random.randrange(6,100)
	for number in range (2, test):
		if test % number == 0:
			return returnRandPrime()
	return test
#Returns a list of possible public keys (e's) to use for message encryption/decryption, does this by ensuring the number returned is relatively prime to the product n and the totient phi. 
def getPossiblePublicKeys(n, phi):
	possible_publickeys =[]
	for number in range(2,phi):
		if gcd(n, number) ==1 and gcd(phi,number) == 1:
			possible_publickeys.append(number)
	return possible_publickeys
#Returns a list of possible private keys (d's) to use for message encryption/decryptionl, does this by checking if the number multiplied with the chosen public key (e) then modulo'd by the totient phi is equal to 1. 
def getPossiblePrivateKeys(e, phi):
	possible_privatekeys = []
	for number in range(phi+1, phi + 1000):
		if (number*e)%phi ==1:
			possible_privatekeys.append(number)
	if len(possible_privatekeys) == 0:
		return getPossiblePrivateKeys(e, phi + 100) #Range changed in case no values were found for possible private keys.
	return possible_privatekeys
#Encrypts or decrypts the message passed by changing the ascii value using the formula x^(m) % n, where x is the ascii value of the character, m is e or d, and n is the product.
def decrypt_encrypt_message(exponent, message):
	encrypted_message = ""
	for letter in message:
		ascii = ord(letter) ** exponent  % n
		encrypted_message += chr(ascii)
	return encrypted_message
p = returnRandPrime() #Random prime 1
q = returnRandPrime() #Random prime 2
while q == p: #Ensure the randomly selected primes aren't the same number
	q = returnRandPrime()
n = p*q 
phi = (p-1) * (q-1) #Calculate Euler's totient

print("Randomly selected primes are " + str(p) + " and " + str(q) + ".")

print("Their product (n) is " + str(n))

print("The number of coprimes relative to n and between 1 and n (phi) is: " + str(phi))

publickeys = getPossiblePublicKeys(n, phi)
print("List of possible values for public keys (e's):\n" + str(publickeys))

e = publickeys[random.randrange(0,len(publickeys))]

print("Randomly selected public key (e) is: " + str(e))

privatekeys = getPossiblePrivateKeys(e, phi)

print("List of possible values for private keys (d's):\n" + str(privatekeys))
d = privatekeys[random.randrange(0,len(privatekeys))]


print("Randomly selected private key (d) is: " + str(d))

message = input("Enter message to encrypt: \n")

encrypted_message = decrypt_encrypt_message(e, message)

print("The encrypted version of the message is: \n" + encrypted_message)
decrypted_message = decrypt_encrypt_message(d, encrypted_message)
print("Message after being decrypted for proof: \n" + decrypted_message)

