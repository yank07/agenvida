from django.db import models

# Create your models here.



from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


    
class Vinculacion(models.Model):
    vinculacion = models.CharField(max_length=50)
    
    def __unicode__(self):
        return '%s' % (self.vinculacion)
    
class Proposito(models.Model):
    usuario = models.ForeignKey(User,related_name='propositos', on_delete=models.CASCADE )
    vinculacion = models.ForeignKey(Vinculacion,related_name='propositos', blank=True, null=True,on_delete=models.CASCADE )
    mes_ano = models.DateField()
    proposito = models.TextField()
    
    def __unicode__(self):
        return '%s' % unicode(self.proposito)
    
class Marcacion(models.Model):
    usuario = models.ForeignKey(User, related_name='marcaciones',  on_delete=models.CASCADE)
    proposito = models.ForeignKey(Proposito,related_name='marcaciones', on_delete=models.CASCADE )    
    dia = models.DateField()
    cumplimiento = models.IntegerField()
   
   
    def __unicode__(self):
        return '%s' %(self.cumplimiento)
    
class Tipo_marcacion(models.Model):
    tipo = models.CharField(max_length=50)
    RangoSup = models.IntegerField()
    RangoInf = models.IntegerField()
    
    def __unicode__(self):
        return '%s' % unicode(self.tipo)


class Oracion (models.Model):
    nombre = models.CharField(max_length=50)
    contenido = RichTextField()
    def __unicode__(self):
        return '%s' % unicode(self.nombre)



class UserPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=100, blank=True, null=True, default="es")
    nacimiento = models.DateField(blank=True, null=True)
    ideal_personal = models.TextField(blank=True, null=True)
    reafirmar = models.TextField(blank=True, null=True)
    liberar = models.TextField(blank=True, null=True)
    adquirir = models.TextField(blank=True, null=True)
    


    def __unicode__(self):
        return '%s' % unicode(self.user)
