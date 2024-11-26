import itertools 
import string

def brute(passoword):
    chars = string.printable.strip()
    a = 0
    for length in range(1, len(password) + 1):
        for guess in itertools.product(chars, repeat=length):
            a += 1
            guess = ''.join(guess)
            if guess == password:
                return (a, guess)
    return (a, None) 
password = input("Enter paswword to crack: ")
a, guess = brute(password)
if guess:
    print(f"password cracket]d at {a} attempt and {guess} password")
else:
    print(f" password not cracked in {a} attemmpts")
