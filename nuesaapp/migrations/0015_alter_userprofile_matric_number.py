# Generated by Django 5.0.1 on 2024-02-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuesaapp', '0014_delete_votestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='matric_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
