# Generated by Django 3.1.3 on 2021-01-31 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0009_auto_20201121_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylistitem',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='grocerylistitem',
            name='ingredient_id',
            field=models.IntegerField(null=True),
        ),
    ]