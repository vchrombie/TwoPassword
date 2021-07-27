import os
from cryptography.fernet import Fernet

from twopassword.settings import BASE_DIR

KEY_FILE_PATH = os.path.join(BASE_DIR, "secret.key")


def encrypt(decrypted_password):
    key = load_key()
    f = Fernet(key)

    encoded_password = decrypted_password.encode()
    encrypted_password = f.encrypt(encoded_password)

    return encrypted_password.decode('utf-8')


def decrypt(encrypted_password):
    key = load_key()
    f = Fernet(key)

    encoded_password = encrypted_password.encode()
    decrypted_password = f.decrypt(encoded_password)

    return decrypted_password.decode('utf-8')


def load_key():
    return open(KEY_FILE_PATH, "rb").read()


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE_PATH, "wb") as key_file:
        key_file.write(key)


if __name__ == '__main__':
    generate_key()
