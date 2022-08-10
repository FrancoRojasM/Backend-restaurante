from django.db import models

# Create your models here.

class Categoria(models.Model):
    id= models.AutoField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen= models.TextField(default="https://www.google.com/")
    class Meta:
        db_table='categorias'
        ordering=['id']


