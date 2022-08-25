# Generated by Django 4.1 on 2022-08-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.TextField(default='https://www.google.com/')),
            ],
            options={
                'db_table': 'categorias',
                'ordering': ['id'],
            },
        ),
    ]
