# Generated by Django 3.0.5 on 2020-04-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20200407_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(),
        ),
    ]
