# Generated by Django 4.0.5 on 2022-06-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('clase', models.CharField(max_length=255)),
                ('empresa', models.CharField(max_length=255)),
                ('dado_de_baja', models.BooleanField(default=False)),
            ],
        ),
    ]
