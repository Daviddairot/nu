# Generated by Django 5.0.1 on 2024-02-03 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuesaapp', '0009_votestatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votestatus',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='VoteStatus',
        ),
    ]
