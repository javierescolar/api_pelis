# Generated by Django 2.2.4 on 2019-08-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_peliculafavorita'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='favoritos',
            field=models.IntegerField(default=0),
        ),
    ]
