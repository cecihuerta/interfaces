# Generated by Django 2.0.1 on 2018-06-28 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0006_preparacion_hora_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieta',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interfaces.Paciente'),
        ),
    ]