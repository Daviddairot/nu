# Generated by Django 5.0.1 on 2024-02-03 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuesaapp', '0005_p_r_o1_p_r_o2'),
    ]

    operations = [
        migrations.CreateModel(
            name='assistant_general_secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='assistant_social_director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='candidate_pics/')),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
    ]
