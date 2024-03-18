# Import Model Django
from django.db import models
# Local Managers
from .managers import ReporteLABManager

# Create your models here.

# Generating Tokens by using signals
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# ***********************************************************************************
# ***********************************************************************************
# ***********************************************************************************  
class ReporteLAB(models.Model):
    tipo = models.CharField('Tipo', max_length=4, blank=True, null=True)
    cemento = models.CharField('Cemento', max_length=60, blank=True, null=True)
    productoid = models.PositiveIntegerField('ProductoId', blank=True, null=True)
    cargarpromedioid = models.PositiveIntegerField('CargarPromedioId', blank=True, null=True)
    datetime = models.DateTimeField('C_Fecha', blank=True, null=True)
    month = models.CharField('D_Mes', max_length=15, blank=True, null=True)
    week =  models.PositiveIntegerField('E_Semana', blank=True, null=True)
    proc_clinker = models.CharField('F_Proc_Clinker', max_length=60, blank=True, null=True)
    molino = models.CharField('G_Molino', max_length=15, blank=True, null=True)
    silo = models.CharField('H_Destino', max_length=15, blank=True, null=True)
    fanalista = models.CharField('V_FAnalista', max_length=30, blank=True, null=True)
    qanalista = models.CharField('BL_QAnalista', max_length=30, blank=True, null=True)
    comentarios = models.CharField('CC_Comentarios', max_length=240, blank=True, null=True)
    blaine_cm2g = models.IntegerField('K_Blaine(cm2/g)', blank=True, null=True)
    retenido325 = models.FloatField('L_Retenido325(%)', blank=True, null=True)
    _330µm = models.FloatField('M_3_30µm(%)', blank=True, null=True)
    autoclave = models.FloatField('N_Autoclave(%)', blank=True, null=True)
    barras14dias = models.FloatField('O_Barras14días(%)', blank=True, null=True)
    contenidoaire = models.FloatField('P_ContenidoAire(%)', blank=True, null=True)
    retencionagua = models.FloatField('Q_RetenciónAgua(%)', blank=True, null=True)
    falsofraguado = models.FloatField('R_FalsoFraguado(%)', blank=True, null=True)
    consistencianormal = models.FloatField('S_ConsistenciaNormal(%)', blank=True, null=True)
    fraguadoi = models.IntegerField('T_FraguadoInicial', blank=True, null=True)
    fraguadof = models.IntegerField('U_FraguaFinal', blank=True, null=True)
    aguacemento = models.FloatField('W_AguaCemento(%)', blank=True, null=True)
    flujo = models.FloatField('X_Flujo', blank=True, null=True)
    r1cubo1 = models.FloatField('Y_R1Diacubo1', blank=True, null=True)
    r1cubo2 = models.FloatField('Z_R1Diacubo2', blank=True, null=True)
    r1cubo3 = models.FloatField('AA_R1Diacubo3', blank=True, null=True)
    r1 = models.FloatField('AB_R1Dia', blank=True, null=True)
    r3cubo1 = models.FloatField('AC_R3Diacubo1', blank=True, null=True)
    r3cubo2 = models.FloatField('AD_R3Diacubo2', blank=True, null=True)
    r3cubo3 = models.FloatField('AE_R3Diacubo3', blank=True, null=True)
    r3 = models.FloatField('AF_R3Dia', blank=True, null=True)
    r7cubo1 = models.FloatField('AG_R7Diacubo1', blank=True, null=True)
    r7cubo2 = models.FloatField('AH_R7Diacubo2', blank=True, null=True)
    r7cubo3 = models.FloatField('AI_R7Diacubo3', blank=True, null=True)
    r7 = models.FloatField('AJ_R7Dia', blank=True, null=True)
    r28cubo1 = models.FloatField('AK_R28Diacubo1', blank=True, null=True)
    r28cubo2 = models.FloatField('AL_R28Diacubo2', blank=True, null=True)
    r28cubo3 = models.FloatField('AM_R28Diacubo3', blank=True, null=True)
    r28 = models.FloatField('AN_R28Dia', blank=True, null=True)
    densidad = models.FloatField('AS_Densidad_p(g/cm3)', blank=True, null=True)
    sio2 = models.FloatField('AT_%SiO2', blank=True, null=True)
    ai2o3 = models.FloatField('AU_%AI2O3', blank=True, null=True)
    fe2o3 = models.FloatField('AV_Fe2O3%', blank=True, null=True)
    cao = models.FloatField('AW_%CaO', blank=True, null=True)
    mgo = models.FloatField('AX_%MgO', blank=True, null=True)
    so3 = models.FloatField('AY_%SO3', blank=True, null=True)
    na2o = models.FloatField('AZ_%Na2O', blank=True, null=True)
    k2o = models.FloatField('BA_%K2O', blank=True, null=True)
    tio2 = models.FloatField('BB_%TiO2', blank=True, null=True)
    p2o5 = models.FloatField('BC_%P2O5', blank=True, null=True)
    pi = models.FloatField('BD_%PI', blank=True, null=True)
    callibre = models.FloatField('BE_%Callibre', blank=True, null=True)
    ri = models.FloatField('BG_%RI', blank=True, null=True)
    c3s = models.FloatField('BH_%C3S', blank=True, null=True)
    c2s = models.FloatField('BI_%C2S', blank=True, null=True)
    c3a = models.FloatField('BJ_%C3A', blank=True, null=True)
    c4af = models.FloatField('BK_%C4AF', blank=True, null=True)
    toneladas = models.FloatField('BM_Toneladas', blank=True, null=True)

    # Importo modelos avanzados de Manager
    objects = ReporteLABManager()
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
        verbose_name = 'ReporteLAB'  # Nombre de Columna singular
        verbose_name_plural = 'ReportesLAB'  # Nombre en plural

    # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
        return str(self.id) + ' - ' +str(self.datetime) 