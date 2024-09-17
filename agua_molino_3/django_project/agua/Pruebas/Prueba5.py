# Import send_mail  
from send_mail import mail
mail['body'] = 'Buenos días, este es un email de envio automático de Q&P Tech Panama Inc. \n' # No funciona
mail("jgarcia@qptechllc.com", "Consumo de Agua del Molino 3, Planta Argoa Panamá", "ConsumoDeAguaMolino3_16-9-2024.xlsx", "C:/QPTECH/EXCEL/AGUA_MOLINO3/ConsumoDeAguaMolino3_16-9-2024.xlsx")