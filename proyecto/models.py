from django.db import models

class cancion(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    genero = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)

    def __str__(self):
        return f"nombre: {self.nombre}"

    def delete(self, using=None, keep_parents=False):
        if self.imagen:
            self.imagen.storage.delete(self.imagen.name)
        super().delete(using=using, keep_parents=keep_parents)
