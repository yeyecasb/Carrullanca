# Generated by Django 4.2.3 on 2023-07-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrullancapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='estado_civil',
            field=models.CharField(default='soltero', max_length=50),
            preserve_default=False,
        ),
    ]