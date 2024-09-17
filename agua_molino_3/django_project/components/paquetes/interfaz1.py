# Interfaz Grafica
from tkinter import *
from tkinter import ttk
def ventana1():
    root = Tk()
    root.geometry('200x200')  # Se define el tamanio
    # Permite modificar el tamanio de la Ventana (True o False) (1 o 0)
    root.resizable(True, True)
    # Se define la ruta y el archivo OJO, genera errores
    root.iconbitmap(r'static\images\QPTECH.ico')

    # Modificando mi interfaz o ventana
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text=" Por favor espere que termine ").grid(column=1, row=0)
    ttk.Label(frm, text="  ").grid(column=1, row=1)
    ttk.Button(frm, text="Cerrar", command=root.destroy).grid(column=1, row=5)
    root.mainloop()
