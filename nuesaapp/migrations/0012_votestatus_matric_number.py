# Generated by Django 5.0.1 on 2024-02-03 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuesaapp', '0011_userprofile_votestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='votestatus',
            name='matric_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]