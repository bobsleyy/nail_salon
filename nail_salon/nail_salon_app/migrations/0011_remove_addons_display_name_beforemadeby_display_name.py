# Generated by Django 4.2.7 on 2023-12-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail_salon_app', '0010_addons_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addons',
            name='display_name',
        ),
        migrations.AddField(
            model_name='beforemadeby',
            name='display_name',
            field=models.CharField(default='yes', max_length=64),
            preserve_default=False,
        ),
    ]
