# Generated by Django 2.2.5 on 2019-09-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190920_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='film_runtime',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
