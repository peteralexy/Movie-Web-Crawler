# Generated by Django 2.2.5 on 2019-09-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]