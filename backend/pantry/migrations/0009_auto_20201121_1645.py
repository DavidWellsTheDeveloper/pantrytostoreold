# Generated by Django 3.1.3 on 2020-11-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0008_grocerylistitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylistitem',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
