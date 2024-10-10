from django.db import models
from django.contrib.auth.models import User

class Sokajy(models.Model):
    anarana = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('anarana',)
        verbose_name_plural = 'Sokajy'
        
    def __str__(self):
        return self.anarana
    

class Entambarotra(models.Model):
    sokajy = models.ForeignKey(Sokajy, related_name='items', on_delete=models.CASCADE )
    anarana = models.CharField(max_length=255)
    fanazavana = models.TextField(blank=True, null=True)
    vidiny = models.FloatField() 
    sary = models.ImageField(upload_to='item_images', blank=True, null=True, default='item_images/default.jpg')
    lafo_ve = models.BooleanField(default=False)
    mpivarotra = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    daty = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.anarana
    
    class Meta:
        ordering = ('anarana',)
        verbose_name_plural = 'Etambarotra'
    
 