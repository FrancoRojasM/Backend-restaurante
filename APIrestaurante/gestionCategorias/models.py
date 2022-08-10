from django.db import models

from adminUsuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    id= models.AutoField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen= models.TextField(default="https://www.google.com/")
    # creando la relacion entre el modelo tarea y usuario
    # on_delete > sirve para indicar que accion se debe de realizar sobre los registros que pertenecen a ese registro a eliminar
    # CASCADE: se elimina el usuario y se procede a eliminar a sus tareas
    # PROTECT: evita la elimnacion del suuario y emitira un error
    # SET_NULL: elimina el usuario y a todas sus tareas les cambia el valor de admin_id a NULL
    # SET_DEFAULT: elimina el usuario y modifica su valor a un valor por defecto
    # related_name: sirve para que a raiz del modelo usuario este cree un atributo en la clase Usuario para poder accder a todas sus tareas si no se define el valor predeterminado sera usuario_set_categoria
    adminId=models.ForeignKey(to=Usuario,related_name='categorias',db_column='admin_id', on_delete=models.CASCADE)


    class Meta:
        db_table='categorias'
        ordering=['id']


