# Generated by Django 3.1.3 on 2020-11-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0004_auto_20201121_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylistitem',
            name='unit',
            field=models.CharField(max_length=50, null=True),
        ),
    ]