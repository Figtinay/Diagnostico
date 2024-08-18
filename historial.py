# historial.py
import tkinter as tk
import tkinter.ttk as ttk
import csv

def show_history(root):
    history_window = tk.Toplevel(root)
    history_window.title('Historial de Diagnósticos')
    history_window.geometry('900x400')

    tree = ttk.Treeview(history_window, columns=('Fecha', 'Nombre', 'Cédula', 'Diagnóstico'), show='headings')
    tree.heading('Fecha', text='Fecha')
    tree.heading('Nombre', text='Nombre')
    tree.heading('Cédula', text='Cédula')
    tree.heading('Diagnóstico', text='Diagnóstico')
    tree.pack(fill=tk.BOTH, expand=True)

    with open('diagnosticos.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert('', tk.END, values=row)

    close_button = ttk.Button(history_window, text='Cerrar', command=history_window.destroy)
    close_button.pack(pady=10)