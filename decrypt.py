from cryptography.fernet import Fernet
import os

def decrypt(file_path, key_entry, file_label, encryption_key=None):
    if encryption_key is None:
        encryption_key = key_entry.get().encode()
    f = Fernet(encryption_key)
    
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    original_file_path = file_path.replace('.bread', '')
    
    with open(original_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    os.remove(file_path)
    file_label.configure(text=original_file_path)
    
    return original_file_path

