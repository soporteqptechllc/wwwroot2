# Import datetime  
from datetime import date
# Import send_mail  
from send_mail import mail
# Import tkinter 
from tkinter import ttk, Tk

# Interfaz Grafica
root = Tk()
root.geometry('400x150')  # Se define el tamanio
# Permite modificar el tamanio de la Ventana (True o False) (1 o 0)
root.resizable(True, True)
# Se define la ruta y el archivo OJO, genera errores
#root.iconbitmap(r"Ejemplos\yinyan.ico")
root.iconbitmap("C:/inetpub/django_project/static/images/Argos.ico")

# Modificando mi interfaz o ventana
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Ya se envió el correo y el Excel!",
          font=('Times', '20', 'bold italic'), foreground="blue").grid(column=1, row=0)
#('Helvetica', '16')
ttk.Label(frm, text="").grid(column=1, row=1)
ttk.Button(frm, text="Cerrar", command=root.destroy).grid(column=1, row=5)
# Metodo cerrar ventana
def cerrar():
    root.destroy()
# Espera un tiempo luego ejecuta "cerrar"    
root.after(10000, cerrar)
# Método mainloop el cual es el que mantiene visible la ventana
root.mainloop()