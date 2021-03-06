# Generated by Django 3.2.8 on 2021-11-11 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mission_type', models.CharField(max_length=50)),
                ('launched', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('planet_type', models.CharField(max_length=50)),
                ('mass', models.CharField(max_length=50)),
                ('diameter', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('missions', models.ManyToManyField(blank=True, to='main_app.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('satellite_type', models.CharField(max_length=50)),
                ('mass', models.CharField(max_length=50)),
                ('diameter', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('missions', models.ManyToManyField(blank=True, to='main_app.Mission')),
                ('planet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.planet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('star_type', models.CharField(max_length=50)),
                ('mass', models.CharField(max_length=50)),
                ('diameter', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('missions', models.ManyToManyField(blank=True, to='main_app.Mission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.star')),
            ],
        ),
        migrations.CreateModel(
            name='SatellitePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('satellite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.satellite')),
            ],
        ),
        migrations.CreateModel(
            name='PlanetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.planet')),
            ],
        ),
        migrations.AddField(
            model_name='planet',
            name='star',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.star'),
        ),
        migrations.AddField(
            model_name='planet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
