import random

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime():
    """Generate a random prime number."""
    while True:
        num = random.randint(100, 1000)  # Adjust range as needed
        if is_prime(num):
            return num

def gcd(a, b):
    """Calculate the Greatest Common Divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    """Generate RSA public and private keys."""
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    return ((e, n), (d, n))

# Beispielaufruf der Funktionen
public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)



