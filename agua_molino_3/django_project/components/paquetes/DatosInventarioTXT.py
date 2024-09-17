# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 01:46:05 2021

@author: Administrator
"""
import pandas as pd
# calculos
def cargadedatos():
    import pandas as pd
    # fila vacia para los materiales que no existen en el listado de Equipos --> Material
    dic={'Unnamed: 0': {0: ''},'Saldo al': {0: ''},'Soc.': {0: 'PA04'},'Cta.mayor': {0: 1401130101},'Material': {0: 99999999},'Texto breve de material': {0: 'NO DEFINIDO'},'ÁVal': {0: ''},'       Stock total': {0: 0},'UMB': {0: 'UN'},'Precio variable': {0: 00.00},'       Valor total': {0: 00.00},'CatVa': {0: 0},'Prc': {0: 'V'},'Precio estándar': {0: 0.00},'   por': {0: 1},'Mon.': {0: 'PAB'},'TipVal': {0: 'C'}}
    df0=pd.DataFrame.from_dict(dic, orient='columns', dtype=None, columns=None)

    #lectura de archivo y creacion de DATAFRAME
    df1 = pd.read_csv("media/files/inventario.txt", sep='\t', encoding='latin1')

    #Concatena los dos DATAFRAME para agregar un campo vacio en la primera fila
    df=pd.concat([df0,df1],ignore_index=True)

    #Creacion de engine para la conexion con la base de datos
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://mantenimiento:#Argos2017@localhost:5432/ARGOSDB')

    #Elimina los Materiales repetidos consecutivos (no asi los no consecutivos)
    borrar=[]
    for i in range(len(df.Material)-1):
        if df.Material[i]==df.Material[i+1]:
            suma=float(df['       Stock total'][i])+float(df['       Stock total'][i+1])
            df['       Stock total'][i]=suma
            borrar.append(i+1)
            #print(df.Material[i])
    df2=df.drop(borrar,axis=0)

    #Cambia en nombre del Indice Index
    df2.index.names = ['id']

    #CREA la tabla en la base de datos
    df2.to_sql('inventario', engine, if_exists='replace')
    #df2.to_sql('inventario', engine, if_exists='append')
    #sc = df[["Material","Texto breve de material","       Stock total","UMB","Precio variable","Mon."]]
    #new_df=sc.copy()
    querysql = 'ALTER TABLE inventario ADD PRIMARY KEY (id);'
    engine.execute(querysql)

