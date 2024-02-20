message = int(input("Nachricht: "))
public_e = int(input("Public key(e): "))
public_n = int(input("Public key(n): "))

solution = pow(message, public_e, public_n)
print(f"{solution}")
