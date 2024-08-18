import tkinter as tk

def clear_window(img_label, result_label, name_entry, id_entry):
    img_label.config(image='')
    img_label.image = None
    result_label.config(text='Diagnostico:')
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
