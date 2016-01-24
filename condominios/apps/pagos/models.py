from django.db import models
from apps.venezuela.models import Banco
from apps.usuarios.models import Usuario
"""
Jovan Pacheco

"""         

class TipoDePago(models.Model):
    
    tipoDePago=models.CharField('Tipo de pagos',max_length=100,unique=True)

    def __str__(self):
        return str(self.tipoDePago)

    class Meta:
        #db_table = 'administradora_tipodepago'
        verbose_name_plural = "Tipo de pagos"
        verbose_name = "Tipo de pago"             


class RegistroPago(models.Model):
    
    banco=models.ForeignKey(Banco)
    tipoDePago=models.ForeignKey(TipoDePago)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    referencia=models.CharField(max_length=10,unique=True)
    fecha = models.DateTimeField()
    comentario=models.CharField(max_length=140)
    pagadoPor = models.ForeignKey(Usuario)

    def __str__(self):
        return str(self.banco)

    class Meta:
        #db_table = 'administradora_registropago'
        verbose_name_plural = "Registro de pagos"
        verbose_name = "Registro de pago"           