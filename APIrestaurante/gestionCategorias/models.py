from django.db import models

from adminUsuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    id= models.AutoField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen= models.TextField(default="https://www.google.com/")
    # creando la relacion entre el modelo categorias y usuario    
    adminId=models.ForeignKey(to=Usuario,related_name='categorias',db_column='admin_id', on_delete=models.CASCADE)


    class Meta:
        db_table='categorias'
        ordering=['id']


