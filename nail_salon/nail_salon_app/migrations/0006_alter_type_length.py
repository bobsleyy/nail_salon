# Generated by Django 4.2.7 on 2023-12-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail_salon_app', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='length',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]