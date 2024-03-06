# Generated by Django 4.2.7 on 2023-12-12 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addon', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BeforeMadeBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before_made_by_me', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CostAndTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('execution_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField()),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('second_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('datetime', models.DateTimeField(unique=True)),
                ('addons', models.ManyToManyField(to='nail_salon_app.addons')),
                ('what_to_do', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nail_salon_app.costandtime')),
            ],
        ),
        migrations.AddField(
            model_name='costandtime',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nail_salon_app.servicetype'),
        ),
        migrations.AddField(
            model_name='costandtime',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nail_salon_app.type'),
        ),
    ]
