# Generated by Django 3.2.9 on 2021-12-06 17:37

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
            name='Diver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dumpster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Haul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('image_path', models.ImageField(upload_to='images/')),
                ('diver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rummagerapi.diver')),
                ('dumpster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rummagerapi.dumpster')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('haul_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rummagerapi.haul')),
            ],
        ),
        migrations.AddField(
            model_name='haul',
            name='tags',
            field=models.ManyToManyField(to='rummagerapi.Tag'),
        ),
    ]
