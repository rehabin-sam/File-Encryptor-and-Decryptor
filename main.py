import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from encrypt import encrypt
from decrypt import decrypt
from utils import UploadAction

file_path = ""
encryption_key = None

def upload_and_update_label(file_label):
    global file_path
    file_path = UploadAction(file_label)

def encrypt_and_update_label(file_path, key_entry, file_label):
    global encryption_key
    file_path, encryption_key = encrypt(file_path, key_entry, file_label)

def decrypt_and_update_label(file_path, key_entry, file_label):
    decrypt(file_path, key_entry, file_label, encryption_key)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.geometry("1280x720")
app.title("Bread: File Encrypter and Decryptor")

font_style = ("Montserrat", 14)

bg_image = Image.open("D:/cyber-security/Project/File Encryption System/final/assets/Bread bg.jpg")
bg_image_tk = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(app, image=bg_image_tk)
background_label.place(relwidth=1, relheight=1)

rounded_frame = ctk.CTkFrame(app, corner_radius=20)
rounded_frame.place(relx=0.5, rely=0.5, anchor='center')

file_name = ctk.CTkLabel(rounded_frame, text="File Name:", font=font_style)
file_name.grid(column=0, row=0, padx=20, pady=20)

file_label = ctk.CTkLabel(rounded_frame, text="No file selected", text_color="red", font=font_style)
file_label.grid(column=1, row=0, padx=20, pady=20)

Upload = ctk.CTkButton(rounded_frame, text="Upload File", command=lambda: upload_and_update_label(file_label), font=font_style, corner_radius=20)
Upload.grid(row=0, column=2, padx=10, pady=10)

key_label = ctk.CTkLabel(rounded_frame, text='Key: ', font=font_style)
key_label.grid(column=0, row=1, padx=20, pady=20)

key_entry = ctk.CTkEntry(rounded_frame, width=200, height=40)
key_entry.grid(column=1, columnspan=2, row=1, padx=20, pady=20)

encry = ctk.CTkButton(rounded_frame, text="Encrypt", command=lambda: encrypt_and_update_label(file_path, key_entry, file_label), font=font_style, corner_radius=20)
encry.grid(row=2, column=1, padx=10, pady=10)

decry = ctk.CTkButton(rounded_frame, text="Decrypt", command=lambda: decrypt_and_update_label(file_path, key_entry, file_label), font=font_style, corner_radius=20)
decry.grid(row=2, column=2, padx=10, pady=10)

app.mainloop()
