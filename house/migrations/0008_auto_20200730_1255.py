# Generated by Django 3.0.8 on 2020-07-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20200730_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
