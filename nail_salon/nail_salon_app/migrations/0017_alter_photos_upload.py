# Generated by Django 4.2.7 on 2023-12-15 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail_salon_app', '0016_alter_photos_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='upload',
            field=models.FileField(upload_to=''),
        ),
    ]
