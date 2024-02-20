def decode_block(block, private_key):
    """Decode a single block using the private key."""
    d, n = private_key
    decoded_block = pow(block, d, n)
    return decoded_block


def decrypt_message(encrypted_message, private_key):
    """Decrypt the entire message using the private key."""
    decrypted_message = ""
    block_size = len(str(private_key[1]))  # Assuming block size is the length of n in the private key
    blocks = [int(encrypted_message[i:i + block_size]) for i in range(0, len(encrypted_message), block_size)]

    for block in blocks:
        decoded_block = decode_block(block, private_key)
        decrypted_message += str(decoded_block)

    return decrypted_message


# Eingabe der verschlüsselten Nachricht und des privaten Schlüssels durch den Benutzer
encrypted_message = input("Geben Sie die verschlüsselte Nachricht ein: ")
private_key_d = int(input("Geben Sie den privaten Schlüssel 'd' ein: "))
private_key_n = int(input("Geben Sie den privaten Schlüssel 'n' ein: "))
private_key = (private_key_d, private_key_n)

# Entschlüsselung der Nachricht
decrypted_message = decrypt_message(encrypted_message, private_key)
print("Entschlüsselte Nachricht:", decrypted_message)



