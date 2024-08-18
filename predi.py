import tkinter as tk
from tkinter import filedialog
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import numpy as np
from borrar import clear_window
from guardar import save_diagnosis
from historial import show_history

# Cargar el modelo guardado
model = load_model('modelo_enferm.h5')
categories = ['Quiste', 'Cálculo', 'Tumor', 'Normalidad']

def load_image():
    if not name_entry.get() or not id_entry.get():
        tk.messagebox.showwarning("Advertencia", "Por favor, ingrese su nombre y cédula antes de cargar la imagen.")
        return
    
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path).convert('L')
    img = img.resize((128, 128), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    img_label.config(image=img_tk)
    img_label.image = img_tk

    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    result = categories[np.argmax(prediction)]
    result_label.config(text=f'Diagnóstico: Paciente con {result}')
    # Guardar el diagnóstico con el nombre y la cédula
    save_diagnosis(result, name_entry.get(), id_entry.get())

root = tk.Tk()
root.title('Predicción de Enfermedades')
root.geometry('500x500')

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))

# Frame para los datos del usuario
user_frame = ttk.Frame(root, padding="10")
user_frame.pack(fill='x')

ttk.Label(user_frame, text='Nombre:').pack(anchor='w')
name_entry = tk.Entry(user_frame)
name_entry.pack(fill='x', pady=5)

ttk.Label(user_frame, text='Cédula:').pack(anchor='w')
id_entry = tk.Entry(user_frame)
id_entry.pack(fill='x', pady=5)

# Frame para la imagen y los botones
image_frame = ttk.Frame(root, padding="10")
image_frame.pack(fill='x')

img_label = ttk.Label(image_frame)
img_label.pack(pady=10)

load_button = ttk.Button(image_frame, text='Subir Imagen', command=load_image)
load_button.pack(pady=5)

clear_button = ttk.Button(image_frame, text='Limpiar', command=lambda: clear_window(img_label, result_label, name_entry, id_entry))
clear_button.pack(pady=5)

result_label = ttk.Label(image_frame, text='Diagnóstico:')
result_label.pack(pady=10)

# Frame para los botones de historial y cerrar
action_frame = ttk.Frame(root, padding="10")
action_frame.pack(fill='x')

history_button = ttk.Button(action_frame, text='Ver Historial', command=lambda: show_history(root))
history_button.pack(side='left', padx=5)

close_button = ttk.Button(action_frame, text='Cerrar', command=root.destroy)
close_button.pack(side='right', padx=5)
    
root.mainloop()