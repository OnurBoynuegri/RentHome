# Generated by Django 3.0.8 on 2020-08-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0011_auto_20200801_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
