# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

#Molino3
def cargardatosmolinos3():
    import pandas as pd
    df_equipos = pd.read_excel(
        io="C:/Users/Ingenieria/Desktop/wwwroot/wwwroot/Catalogo/Skote_Django/Admin/media/files1/REPUESTO_POR_AREAS.xlsx", sheet_name="REPUESTO DE MOLINO 3")
    engine = create_engine(
        'postgresql://mantenimiento:#Argos2017@localhost:5432/ARGOSDB')
    df_equipos.index.names = ['id']
    df_equipos.rename(columns={'ÁREA DE PLANTA': 'AREA DE PLANTA', 'UBICACIÓN FUNCIONAL': 'UBICACION FUNCIONAL', 'DESCRIPCIÓN DE UBICACIÓN FUNCIONAL': 'DESCRIPCION DE UBICACION FUNCIONAL',
                  'DESCRIPCIÓN DE EQUIPO': 'EQUIPO_HAC', 'CÓDIGO DE SAP': 'material_id', 'DESCRIPCIÓN DE MATERIAL': 'DESCRIPCION DE MATERIAL'}, inplace=True)
    # Cambia los codigos de los materiales por los id de la tabla de inventario
    df_inventario=pd.read_sql('inventario',engine)
    m_id =0
    for m in df_equipos.material_id:
        if m is not None:
            mask=df_inventario.Material==m
            j=0
            No_encontrado=1
            for i in mask:
                if i:
                    df_equipos.material_id[m_id] = int(df_inventario.id[j])
                    No_encontrado=0
                    #print(j,df_equipos.Material[m_id])
                j +=1
            if No_encontrado:
                df_equipos.material_id[m_id] = 0        
        m_id +=1
    df_equipos.to_sql('molino3', engine, if_exists='replace')
    querysql = 'ALTER TABLE molino3 ADD PRIMARY KEY (id);'
    engine.execute(querysql)
