# Generated by Django 2.2.5 on 2019-09-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20190920_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='movie_runtime',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
