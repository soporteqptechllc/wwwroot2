from mailbox import NoSuchMailboxError
from django.db import models
from django.db.models.deletion import CASCADE


class planta(models.Model):
    Nombre          =   models.TextField(db_column='Planta', blank=True, null=True)
    CodigoPlanta    =   models.BigIntegerField(db_column='CodigoPlanta', blank=True, null=True)

    def __str__(self):
        return str(self.Nombre)+" Codigo de PLanta: "+str(self.CodigoPlanta)
        
class material(models.Model):
    codigo_sap          =   models.IntegerField(db_column='material', blank=True, null=True)
    nombre_material     =   models.TextField(db_column='Nom_material', blank=True, null=True)
    nombre_corto        =   models.CharField(db_column='Nom_corto', max_length=20, blank=True, null=True)
    densidad            =   models.FloatField(blank=True,null=True)

    def __str__(self):
        return str(self.nombre_material)+" Codigo SAP: "+str(self.codigo_sap)+ " Nombre corto: "+str(self.nombre_corto)

# Base de Datos de Planta Tocumen
class silos(models.Model):
    silo                =   models.CharField(db_column='silo', max_length=20, blank=True, null=True)
    planta              =   models.CharField(db_column='planta', max_length=80, blank=True, null=True)
    codigo_sap          =   models.ForeignKey(material, default= 1, on_delete=models.CASCADE,related_name='productos')
    toneladas           =   models.FloatField(db_column='toneladas', blank=True, null=True)
    nivel               =   models.FloatField(db_column='nivel', blank=True, null=True)
    metros              =   models.FloatField(db_column='metros', blank=True, null=True)
    estado_silo         =   models.TextField(db_column='estado_silo', blank=True, null=True)
    fecha_estado_silo   =   models.DateTimeField(db_column='fecha_estado_silo', blank=True, null=True)
    estado_pedido       =   models.TextField(db_column='estado_pedido', blank=True, null=True)
    fecha_estado_pedido =   models.DateTimeField(db_column='fecha_estado_pedido', blank=True, null=True)
    ultimo_llenado      =   models.DateTimeField(db_column='ultimo_llenado', blank=True, null=True)
    radio_cilindro      =   models.FloatField(db_column='radio_cilindro',blank=True, null=True) #(m) Para calcular el volumen del cilindro del SILO m^3 Volumen = Pi * r^2 * h
    altura_cilindro     =   models.FloatField(db_column='altura_cilindro',blank=True, null=True) #(m) Para calcular el volumen maximo del cilindro de SILO m^3
    setpoint            =   models.FloatField(db_column='setpoint',blank=True, null=True) # Valor en Metros desado para mantener el nivel.
    metrosxbotella      =   models.FloatField(db_column='metrosxbotella',blank=True, null=True) # Valor en Metros desado para mantener el nivel.



    def __str__(self):
        return str(self.pk)+" Silo "+str(self.silo) + " material "+ str(self.codigo_sap)

#Base de datos de Silos de Cemento de Mezlcas Listas
class silosML(models.Model):
    silo                =   models.CharField(db_column='silo', max_length=20, blank=True, null=True)
    planta              =   models.CharField(db_column='planta', max_length=80, blank=True, null=True)
    #material            =   models.TextField(db_column='material', blank=True, null=True)
    #codigo_sap          =   models.BigIntegerField(db_column='codigo_sap', blank=True, null=True)
    codigo_sap          =   models.ForeignKey(material, default= 1, on_delete=models.CASCADE,related_name='productosML')
    #description         =   models.TextField(db_column='description', blank=True, null=True)
    toneladas           =   models.FloatField(db_column='toneladas', blank=True, null=True)
    nivel               =   models.FloatField(db_column='nivel', blank=True, null=True)
    metros              =   models.FloatField(db_column='metros', blank=True, null=True)
    estado_silo         =   models.TextField(db_column='estado_silo', blank=True, null=True)
    fecha_estado_silo   =   models.DateTimeField(db_column='fecha_estado_silo', blank=True, null=True)
    estado_pedido       =   models.TextField(db_column='estado_pedido', blank=True, null=True)
    fecha_estado_pedido =   models.DateTimeField(db_column='fecha_estado_pedido', blank=True, null=True)
    ultimo_llenado      =   models.DateTimeField(db_column='ultimo_llenado', blank=True, null=True)
    radio_cilindro      =   models.FloatField(db_column='radio_cilindro',blank=True, null=True) #(m) Para calcular el volumen del cilindro del SILO m^3 Volumen = Pi * r^2 * h
    altura_cilindro     =   models.FloatField(db_column='altura_cilindro',blank=True, null=True) #(m) Para calcular el volumen maximo del cilindro de SILO m^3


    def __str__(self):
        return str(self.pk)+" Silo "+str(self.silo) + " material "+ str(self.codigo_sap)

class llegadas(models.Model):
    llegadas_id          =   models.BigIntegerField(db_column='llegadas_id', blank=True, null=True)            # id de pedido
    description         =   models.TextField(db_column='description', blank=True, null=True)                # Informacion del pedido
    nivel_porcen        =   models.FloatField(db_column='nivel_porcen', blank=True, null=True)              # Porcentaje de Nivel al momento de generla el pedido
    fecha_fin           =   models.DateTimeField(db_column='fecha_fin', blank=True, null=True)           # Fecha se genero el pedido.
    n_maximo            =   models.FloatField(db_column='nivel_maximo', blank=True, null=True)              # Valor maximo punto de partida de la medicion.
    n_minimo            =   models.FloatField(db_column='nivel_minimo', blank=True, null=True)              # Valor maximo punto de partida de la medicion.
    incremento          =   models.FloatField(db_column='incremento', blank=True, null=True)                # Valor que define la botella. Diferencia entre el maximo y minimo
    fecha_min           =   models.DateTimeField(db_column='fecha_min', blank=True, null=True)              # Fecha del punto de inicio de la medicion Valor maximo
    id_sensorLL         =   models.BigIntegerField(db_column='sensor_id', blank=True, null=True)
    planta              =   models.TextField(db_column='planta', blank=True, null=True)
    nom_silo            =   models.TextField(db_column='nombre_silo', blank=True, null=True)

    def __str__(self):
        return str(self.pk)+" Fin llenado: "+str(self.fecha_fin) + " Altura de llenado: "+ str(self.incremento) + " Nivel Alcanzado: "+ str(self.n_maximo)


class pedidos(models.Model):
    pedidos_id          =   models.BigIntegerField(db_column='pedido_id', blank=True, null=True)            # id de pedido
    codigo_sap          =   models.BigIntegerField(db_column='codigo_sap', blank=True, null=True)           # Codigo SAP del Pedido (Tipo de Cemento)
    description         =   models.TextField(db_column='description', blank=True, null=True)                # Informacion del pedido
    toneladas           =   models.FloatField(db_column='toneladas', blank=True, null=True)                 # Toneladas calculadsas restantes en el silo
    nivel_porcen        =   models.FloatField(db_column='nivel_porcen', blank=True, null=True)              # Porcentaje de Nivel al momento de generla el pedido
    nivel_metros        =   models.FloatField(db_column='nivel_metros', blank=True, null=True)              # Nivel en Metros al momento de general el pedido
    estado_pedido       =   models.IntegerField(db_column='estado_pedido', blank=True, null=True)           # 1 pedido abierto y 2 pedido cerrado
    fecha_pedido        =   models.DateTimeField(db_column='fecha_pedido', blank=True, null=True)           # Fecha se genero el pedido.
    fecha_cerrado       =   models.DateTimeField(db_column='fecha_cerrado', blank=True, null=True)          # Fecha que se asume se recibio el pedido.
    ton_max             =   models.FloatField(db_column="ton_max",blank=True, null=True)                    # Valor maximo en toneladas del silo
    n_maximo            =   models.FloatField(db_column='nivel_maximo', blank=True, null=True)              # Valor maximo punto de partida de la medicion.
    decremento          =   models.FloatField(db_column='decremento', blank=True, null=True)                # Valor que define la botella. Diferencia entre el maximo y minimo
    fecha_max           =   models.DateTimeField(db_column='fecha_max', blank=True, null=True)              # Fecha del punto de inicio de la medicion Valor maximo
    id_tablaLlegadas    =   models.BigIntegerField(db_column='llegadas_id', blank=True, null=True)          # id de la table de LLEGADAS de botellas - Match entre pedido y llegadas
    id_sensorP          =   models.BigIntegerField(db_column='sensor_id', blank=True, null=True)
    planta              =   models.TextField(db_column='planta', blank=True, null=True)
    nom_silo            =   models.TextField(db_column='nombre_silo', blank=True, null=True)
    prioridad           =   models.IntegerField(db_column='prioridad', blank=True, null=True)


    def __str__(self):
        return str(self.pk)+" Codigo Producto: "+str(self.codigo_sap) + " Descripcion: "+ str(self.description) + " Fecha: "+ str(self.fecha_pedido)
    
class Valoressensores(models.Model):
    nivel = models.FloatField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    origen = models.TextField(db_column='Origen', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    nombre_silo = models.TextField(db_column='nombre_Silo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ValoresSensores'

#Modelos 