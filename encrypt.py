from cryptography.fernet import Fernet
import tkinter as tk

def encrypt(file_path, key_entry, file_label):
    encryption_key = Fernet.generate_key()
    f = Fernet(encryption_key)
    
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = f.encrypt(original)
    encrypted_file_path = file_path + '.bread'
    
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    key_entry.delete(0, tk.END)
    key_entry.insert(0, encryption_key.decode())
    file_label.configure(text=encrypted_file_path)
    
    return encrypted_file_path, encryption_key
