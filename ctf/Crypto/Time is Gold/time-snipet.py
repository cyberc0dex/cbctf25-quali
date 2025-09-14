    key = timestamp.to_bytes(16, byteorder='big')  # Use 16 bytes for AES
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

