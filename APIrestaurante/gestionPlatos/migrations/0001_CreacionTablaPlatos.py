# Generated by Django 4.1 on 2022-08-20 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionCategorias', '0002_RelacionCategoriaUsuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.TextField(default='https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('stock', models.IntegerField()),
                ('adminId', models.ForeignKey(db_column='admin_id', on_delete=django.db.models.deletion.CASCADE, related_name='platos', to=settings.AUTH_USER_MODEL)),
                ('categoriasId', models.ForeignKey(db_column='categorias_id', on_delete=django.db.models.deletion.CASCADE, related_name='platos', to='gestionCategorias.categoria')),
            ],
            options={
                'db_table': 'platos',
                'ordering': ['id'],
            },
        ),
    ]
