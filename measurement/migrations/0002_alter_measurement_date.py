# Generated by Django 4.0.6 on 2022-08-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]