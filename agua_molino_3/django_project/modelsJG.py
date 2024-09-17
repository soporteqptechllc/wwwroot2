# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class AguaMedidoraguamolino3(models.Model):
    id = models.BigAutoField(primary_key=True)
    datatime_db = models.DateTimeField()
    volumen_totalizado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agua_medidoraguamolino3'


class AguaMedidoraguario(models.Model):
    id = models.BigAutoField(primary_key=True)
    datatime_db = models.DateTimeField()
    datatime_plc = models.DateTimeField(blank=True, null=True)
    volumen_totalizado = models.IntegerField()
    medida_flujo = models.FloatField()
    nivel_tanq = models.FloatField()
    estado_bomba1 = models.IntegerField()
    estado_bomba2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agua_medidoraguario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class ComponentsLlegadas(models.Model):
    llegadas_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nivel_porcen = models.FloatField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    nivel_maximo = models.FloatField(blank=True, null=True)
    nivel_minimo = models.FloatField(blank=True, null=True)
    incremento = models.FloatField(blank=True, null=True)
    fecha_min = models.DateTimeField(blank=True, null=True)
    sensor_id = models.BigIntegerField(blank=True, null=True)
    nombre_silo = models.TextField(blank=True, null=True)
    planta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components_llegadas'


class ComponentsMaterial(models.Model):
    material = models.IntegerField(blank=True, null=True)
    nom_material = models.TextField(db_column='Nom_material', blank=True, null=True)  # Field name made lowercase.
    nom_corto = models.CharField(db_column='Nom_corto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    densidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components_material'


class ComponentsPedidos(models.Model):
    pedido_id = models.BigIntegerField(blank=True, null=True)
    codigo_sap = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    toneladas = models.FloatField(blank=True, null=True)
    nivel_porcen = models.FloatField(blank=True, null=True)
    estado_pedido = models.IntegerField(blank=True, null=True)
    fecha_pedido = models.DateTimeField(blank=True, null=True)
    fecha_cerrado = models.DateTimeField(blank=True, null=True)
    nivel_metros = models.FloatField(blank=True, null=True)
    ton_max = models.FloatField(blank=True, null=True)
    decremento = models.FloatField(blank=True, null=True)
    fecha_max = models.DateTimeField(blank=True, null=True)
    sensor_id = models.BigIntegerField(blank=True, null=True)
    llegadas_id = models.BigIntegerField(blank=True, null=True)
    nivel_maximo = models.FloatField(blank=True, null=True)
    nombre_silo = models.TextField(blank=True, null=True)
    planta = models.TextField(blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components_pedidos'


class ComponentsPlanta(models.Model):
    planta = models.TextField(db_column='Planta', blank=True, null=True)  # Field name made lowercase.
    codigoplanta = models.BigIntegerField(db_column='CodigoPlanta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'components_planta'


class ComponentsSilos(models.Model):
    silo = models.CharField(max_length=20, blank=True, null=True)
    codigo_sap = models.ForeignKey(ComponentsMaterial, models.DO_NOTHING)
    toneladas = models.FloatField(blank=True, null=True)
    nivel = models.FloatField(blank=True, null=True)
    metros = models.FloatField(blank=True, null=True)
    estado_silo = models.TextField(blank=True, null=True)
    fecha_estado_silo = models.DateTimeField(blank=True, null=True)
    estado_pedido = models.TextField(blank=True, null=True)
    fecha_estado_pedido = models.DateTimeField(blank=True, null=True)
    ultimo_llenado = models.DateTimeField(blank=True, null=True)
    altura_cilindro = models.FloatField(blank=True, null=True)
    radio_cilindro = models.FloatField(blank=True, null=True)
    altura_maxima = models.FloatField(blank=True, null=True)
    setpoint = models.FloatField(blank=True, null=True)
    planta = models.CharField(max_length=80, blank=True, null=True)
    metrosxbotella = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components_silos'


class ComponentsSilosml(models.Model):
    silo = models.CharField(max_length=20, blank=True, null=True)
    codigo_sap = models.ForeignKey(ComponentsMaterial, models.DO_NOTHING)
    toneladas = models.FloatField(blank=True, null=True)
    nivel = models.FloatField(blank=True, null=True)
    metros = models.FloatField(blank=True, null=True)
    estado_silo = models.TextField(blank=True, null=True)
    fecha_estado_silo = models.DateTimeField(blank=True, null=True)
    estado_pedido = models.TextField(blank=True, null=True)
    fecha_estado_pedido = models.DateTimeField(blank=True, null=True)
    ultimo_llenado = models.DateTimeField(blank=True, null=True)
    altura_cilindro = models.FloatField(blank=True, null=True)
    radio_cilindro = models.FloatField(blank=True, null=True)
    altura_maxima = models.FloatField(blank=True, null=True)
    planta = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components_silosml'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipos(models.Model):
    area_de_planta = models.TextField(db_column='AREA DE PLANTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ubicacion_funcional = models.TextField(db_column='UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descripcion_de_ubicacion_funcional = models.TextField(db_column='DESCRIPCION DE UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    equipo = models.TextField(db_column='EQUIPO', blank=True, null=True)  # Field name made lowercase.
    equipo_hac = models.TextField(db_column='EQUIPO_HAC', blank=True, null=True)  # Field name made lowercase.
    descripcion_de_material = models.TextField(db_column='DESCRIPCION DE MATERIAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cant_field = models.FloatField(db_column='CANT.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    unidad_de_medida = models.TextField(db_column='UNIDAD DE MEDIDA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.ForeignKey('Inventario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'equipos'


class Inventario(models.Model):
    unnamed_0 = models.FloatField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saldo_al = models.TextField(db_column='Saldo al', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    soc_field = models.TextField(db_column='Soc.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cta_mayor = models.BigIntegerField(db_column='Cta.mayor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.BigIntegerField(db_column='Material')  # Field name made lowercase.
    texto_breve_de_material = models.TextField(db_column='Texto breve de material', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_stock_total = models.TextField(db_column='       Stock total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    umb = models.TextField(db_column='UMB', blank=True, null=True)  # Field name made lowercase.
    precio_variable = models.TextField(db_column='Precio variable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_valor_total = models.TextField(db_column='       Valor total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    catva = models.BigIntegerField(db_column='CatVa', blank=True, null=True)  # Field name made lowercase.
    prc = models.TextField(db_column='Prc', blank=True, null=True)  # Field name made lowercase.
    field_por = models.BigIntegerField(db_column='   por', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    mon_field = models.TextField(db_column='Mon.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tipval = models.TextField(db_column='TipVal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventario'


class Molino3(models.Model):
    area_de_planta = models.TextField(db_column='AREA DE PLANTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ubicacion_funcional = models.TextField(db_column='UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descripcion_de_ubicacion_funcional = models.TextField(db_column='DESCRIPCION DE UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    equipo = models.TextField(db_column='EQUIPO', blank=True, null=True)  # Field name made lowercase.
    equipo_hac = models.TextField(db_column='EQUIPO_HAC', blank=True, null=True)  # Field name made lowercase.
    descripcion_de_material = models.TextField(db_column='DESCRIPCION DE MATERIAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cant_field = models.FloatField(db_column='CANT.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    unidad_de_medida = models.TextField(db_column='UNIDAD DE MEDIDA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.ForeignKey(Inventario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'molino3'
