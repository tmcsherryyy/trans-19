# Generated by Django 3.0.5 on 2020-04-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20200407_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='visit',
        ),
        migrations.AddField(
            model_name='patient',
            name='visit',
            field=models.ManyToManyField(to='system.Visit'),
        ),
    ]