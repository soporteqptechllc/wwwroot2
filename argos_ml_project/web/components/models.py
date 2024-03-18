from django.db import models



class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.DateTimeField("date published")


class Responsables(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class CentroDeCostos(models.Model):
    area = models.CharField(max_length=200)
    empresa= models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Ingenieros(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)


class encabezado(models.Model):
    cliente = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    contacto = models.ForeignKey(Responsables, on_delete=models.CASCADE)
    area = models.ForeignKey(CentroDeCostos, on_delete=models.CASCADE)
    ingeniero = models.ForeignKey(Ingenieros, on_delete=models.CASCADE)
    
class reportehoras(models.Model):
    encabezado = models.ForeignKey(encabezado, default=1 ,on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    horainicio = models.TimeField()
    horafinal = models.TimeField()
    descripcion = models.CharField(max_length=400)
    finalizacion = models.CharField(max_length=200)


class producciondiaria(models.Model):
    codigo = models.CharField(max_length=30)
    Nombre = models.CharField(max_length=40)
    setpoint = models.FloatField(default=0)
    ho1 = models.CharField(max_length=20, blank=True, null=True)
    op1 = models.FloatField(default=0)
    ho2 = models.CharField(max_length=20, blank=True, null=True)
    op2 = models.FloatField(default=0)
    ho3 = models.CharField(max_length=20, blank=True, null=True)
    op3 = models.FloatField(default=0)
    ho4 = models.CharField(max_length=20, blank=True, null=True)
    op4 = models.FloatField(default=0)
    ho5 = models.CharField(max_length=20, blank=True, null=True)
    op5 = models.FloatField(default=0)
    ho6 = models.CharField(max_length=20, blank=True, null=True)
    op6 = models.FloatField(default=0)
    ho7 = models.CharField(max_length=20, blank=True, null=True)
    op7 = models.FloatField(default=0)
    ho8 = models.CharField(max_length=20, blank=True, null=True)
    op8 = models.FloatField(default=0)
    ho9 = models.CharField(max_length=20, blank=True, null=True)
    op9 = models.FloatField(default=0)
    ho10 = models.CharField(max_length=20, blank=True, null=True)
    op10 = models.FloatField(default=0)
    ho11 = models.CharField(max_length=20, blank=True, null=True)
    op11 = models.FloatField(default=0)
    ho12 = models.CharField(max_length=20, blank=True, null=True)
    op12 = models.FloatField(default=0)
    ho13 = models.CharField(max_length=20, blank=True, null=True)
    op13 = models.FloatField(default=0)
    ho14 = models.CharField(max_length=20, blank=True, null=True)
    op14 = models.FloatField(default=0)
    ho15 = models.CharField(max_length=20, blank=True, null=True)
    op15 = models.FloatField(default=0)
    ho16 = models.CharField(max_length=20, blank=True, null=True)
    op16 = models.FloatField(default=0)
    ho17 = models.CharField(max_length=20, blank=True, null=True)
    op17 = models.FloatField(default=0)
    ho18 = models.CharField(max_length=20, blank=True, null=True)
    op18 = models.FloatField(default=0)
    ho19 = models.CharField(max_length=20, blank=True, null=True)
    op19 = models.FloatField(default=0)
    ho20 = models.CharField(max_length=20, blank=True, null=True)
    op20 = models.FloatField(default=0)
    total = models.FloatField(default=0)
    Editable = models.BooleanField(default=False)
    fecha = models.CharField('fecha',max_length=20, blank=True, null=True) 
     
    def __str__(self):
      return str(self.id) + '-' + self.Nombre