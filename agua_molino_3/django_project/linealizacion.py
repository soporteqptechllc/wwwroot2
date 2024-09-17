import numpy as np
data=[12,34,29,38,34,51,29,34,47,34,55,94,68,81]
x=np.arange(0,len(data))    # definicion de eje X
y = np.array(data)          # Convierte a la lista en un vector de numpy
z = np.polyfit(x,y,1)       # Define el polinomio de aproximacion a la recta.