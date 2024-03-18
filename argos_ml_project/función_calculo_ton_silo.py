# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:17:42 2024

@author: aku.alvarado
"""
def calculo_ton_silos(Nivel_metros_s1,Nivel_metros_s2,Nivel_metros_s3,Nivel_metros_s4,Nivel_metros_s5,Nivel_metros_s6):
 # recibe los niveles de los silos en metros y los retorna una lista con los valores en toneladas en el mismo orden
  import pandas as pd
  from datetime import datetime
  # valores de medición manual maximos con cintas
  silo_arena_cinta = 6.590000000000001
  silo_cemento_cinta = 5.83
  # Getting the current date
  current_date = datetime.now().strftime("%d.%m.%Y")

  # Initializing the variables for silo levels
  nivel_Silo1 = silo_arena_cinta - Nivel_metros_s1
  nivel_Silo2 = silo_arena_cinta - Nivel_metros_s2
  nivel_Silo3 = silo_arena_cinta - Nivel_metros_s3
  nivel_Silo4 = silo_arena_cinta - Nivel_metros_s4
  nivel_Silo5 = silo_cemento_cinta - Nivel_metros_s5
  nivel_Silo6 = silo_cemento_cinta - Nivel_metros_s6

  # Creating the list of silos with their values
  silo_list = [

    #silo1
   {'Capacidad Cilindro': 75.901056,
    'Medida Silo': nivel_Silo1,
    'Volumen Cono': 6.911519999999999,
    'Capacidad Silo': 0,
    'Fecha de Medicion': current_date,
    'Volumen Real': 0,
    'Porcentaje Real Ocupado': 0,
    'Masa Unitaria Arena': 1.55,
    'Toneladas': 0},

    #silo2
   {'Capacidad Cilindro': 75.901056,
    'Medida Silo': nivel_Silo2,
    'Volumen Cono': 6.911519999999999,
    'Capacidad Silo': 0,
    'Fecha de Medicion': current_date,
    'Volumen Real': 0,
    'Porcentaje Real Ocupado': 0,
    'Masa Unitaria Arena': 1.55,
    'Toneladas': 0},

    #silo3
   {'Capacidad Cilindro': 75.901056,
    'Medida Silo': nivel_Silo3,
    'Volumen Cono': 6.911519999999999,
    'Capacidad Silo': 0,
    'Fecha de Medicion': current_date,
    'Volumen Real': 0,
    'Porcentaje Real Ocupado': 0,
    'Masa Unitaria Arena': 1.55,
    'Toneladas': 0},

    #silo4
   {'Capacidad Cilindro': 75.901056,
    'Medida Silo': nivel_Silo4,
    'Volumen Cono': 6.911519999999999,
    'Capacidad Silo': 0,
    'Fecha de Medicion': current_date,
    'Volumen Real': 0,
    'Porcentaje Real Ocupado': 0,
    'Masa Unitaria Arena': 1.32,
    'Toneladas': 0},

    #silo5
   {'Capacidad Cilindro': 76.8180105,
    'Medida Silo': nivel_Silo5,
    'Volumen Cono': 15.90435,
    'Capacidad Silo': 0,
    'Fecha de Medicion': current_date,
    'Volumen Real': 0,
    'Porcentaje Real Ocupado': 0,
    'Masa Unitaria Arena': 1.1,
    'Toneladas': 0},

    #silo6
   {'Capacidad Cilindro': 76.8180105,
    'Medida Silo': nivel_Silo6,
    'Volumen Cono': 15.90435,
    'Capacidad Silo': 0,
    'Fecha de Medicion': current_date,
    'Volumen Real': 0,
    'Porcentaje Real Ocupado': 0,
    'Masa Unitaria Arena': 1.1,
    'Toneladas': 0}
    ]

  # Creating the dictionaries for each silo
  silo1 = silo_list[0]
  silo2 = silo_list[1]
  silo3 = silo_list[2]
  silo4 = silo_list[3]
  silo5 = silo_list[4]
  silo6 = silo_list[5]

  # Calculating each silo's values
  for i in range(0, 4):
      current_silo = silo_list[i]
      current_silo["Capacidad Silo"] = current_silo["Capacidad Cilindro"] + current_silo["Volumen Cono"]
      current_silo["Volumen Real"] = (3.1416*2*2*(1.51*4-current_silo["Medida Silo"])) + current_silo["Volumen Cono"]
      current_silo["Porcentaje Real Ocupado"] = current_silo["Volumen Real"] / current_silo["Capacidad Silo"]
      current_silo["Toneladas"] = current_silo["Volumen Real"] * current_silo["Masa Unitaria Arena"]

  for i in range(4, 6):
      current_silo = silo_list[i]
      current_silo["Capacidad Silo"] = current_silo["Capacidad Cilindro"] + current_silo["Volumen Cono"]
      current_silo["Volumen Real"] = (3.1416*2.25*2.25*(4.83-current_silo["Medida Silo"])) + current_silo["Volumen Cono"]
      current_silo["Porcentaje Real Ocupado"] = current_silo["Volumen Real"] / current_silo["Capacidad Silo"]
      current_silo["Toneladas"] = current_silo["Volumen Real"] * current_silo["Masa Unitaria Arena"]

  # Creating an output of "Toneladas" in a list
  ton_list = []
  for i, silo in enumerate(silo_list, start=1):
      ton_list.append(round(silo['Toneladas'],3))
      #print(f"Silo {i} - Toneladas: {round(silo['Toneladas'],3)}")
  return ton_list

# Código Python para probar la función de calculo de toneladas
Nivel_metros_s1 = 2
Nivel_metros_s2 = 3
Nivel_metros_s3 = 4
Nivel_metros_s4 = 5
Nivel_metros_s5 = 1.5
Nivel_metros_s6 = 2.5
Lista_Silos_toneladas = calculo_ton_silos(Nivel_metros_s1,Nivel_metros_s2,Nivel_metros_s3,Nivel_metros_s4,Nivel_metros_s5,Nivel_metros_s6)
print(Lista_Silos_toneladas)