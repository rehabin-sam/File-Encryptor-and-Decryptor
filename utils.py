from tkinter import filedialog as fd

def UploadAction(file_label):
    file_path = fd.askopenfilename()
    if file_path:
        file_label.configure(text=file_path, text_color="white")
    return file_path
