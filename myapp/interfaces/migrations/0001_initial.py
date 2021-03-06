# Generated by Django 2.0.6 on 2018-06-28 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorias', models.FloatField(blank=True, null=True)),
                ('sodio', models.FloatField(blank=True, null=True)),
                ('potacio', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=31)),
                ('apellido', models.CharField(max_length=31)),
                ('edad', models.IntegerField(default=0)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('estatura', models.FloatField(default=0.0)),
                ('cuenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('enfermedad', models.ManyToManyField(blank=True, null=True, to='interfaces.Enfermedad')),
            ],
        ),
        migrations.CreateModel(
            name='Preparacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=31)),
                ('compuesto_por', models.ManyToManyField(to='interfaces.Alimento')),
                ('pertenece_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfaces.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='preparacion_hora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('dieta', models.ManyToManyField(to='interfaces.Dieta')),
                ('preparacion', models.ManyToManyField(to='interfaces.Preparacion')),
            ],
        ),
        migrations.AddField(
            model_name='alimento',
            name='informacion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='interfaces.Informacion'),
        ),
    ]
