# Generated by Django 3.0.8 on 2020-08-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200811_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='ordernumber',
            field=models.IntegerField(),
        ),
    ]
