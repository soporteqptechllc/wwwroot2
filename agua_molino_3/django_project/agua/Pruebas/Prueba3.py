# Import datetime  
from datetime import date
# Import send_mail  
from send_mail import mail
# Import tkinter 
from tkinter import ttk, Tk
fecha = list()
fecha = ['01','01','2023']
year = date.today().year # current year
month = date.today().month # current month
day = date.today().day # current day
week = date.today().isocalendar()[1] # current week from year
fecha[0] = day
fecha[1] = month
fecha[2] = year
file_name = str(f"ConsumoDeAguaMolino3_{fecha[0]}-{fecha[1]}-{fecha[2]}.xlsx")
file_path = str(f"C:/QPTECH/EXCEL/AGUA_MOLINO3/ConsumoDeAguaMolino3_{fecha[0]}-{fecha[1]}-{fecha[2]}.xlsx")
#print(file_name)
#print(file_path)
# Envió de los correos con el archivo adjunto
#mail("jgarcia@qptechllc.com", "Consumo de Agua del Molino 3, Planta Argoa Panamá", file_name, file_path)

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