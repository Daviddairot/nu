# Generated by Django 5.0.1 on 2024-02-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuesaapp', '0002_vice_president'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financial_Secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='General_Secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Public_Relations_Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Social_Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sports_Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Technical_Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Treasurer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
    ]