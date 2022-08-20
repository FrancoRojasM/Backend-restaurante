from django.db import models

from adminUsuarios.models import Usuario

from gestionCategorias.models import Categoria
# Create your models here.

class Platos(models.Model):
    id= models.AutoField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen= models.TextField(default="https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    # creando la relacion entre el modelo tarea y usuario
    # on_delete > sirve para indicar que accion se debe de realizar sobre los registros que pertenecen a ese registro a eliminar
    # CASCADE: se elimina el usuario y se procede a eliminar a sus tareas
    # PROTECT: evita la elimnacion del suuario y emitira un error
    # SET_NULL: elimina el usuario y a todas sus tareas les cambia el valor de admin_id a NULL
    # SET_DEFAULT: elimina el usuario y modifica su valor a un valor por defecto
    # related_name: sirve para que a raiz del modelo usuario este cree un atributo en la clase Usuario para poder accder a todas sus tareas si no se define el valor predeterminado sera usuario_set_categoria
    precio=models.DecimalField(max_digits=4,decimal_places=2)
    stock=models.IntegerField()
    adminId=models.ForeignKey(to=Usuario,related_name='platos',db_column='admin_id', on_delete=models.CASCADE)
    categoriasId=models.ForeignKey(to=Categoria,related_name='platos',db_column='categorias_id',on_delete=models.CASCADE)

    class Meta:
        db_table='platos'
        ordering=['id']
