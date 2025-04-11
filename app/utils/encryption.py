from cryptography.fernet import Fernet

def encrypt_data(data: bytes, key: str) -> bytes:
    fernet = Fernet(key.encode()) 
    return fernet.encrypt(data)

def decrypt_data(data: bytes, key: str) -> bytes:
    fernet = Fernet(key.encode()) 
    return fernet.decrypt(data)