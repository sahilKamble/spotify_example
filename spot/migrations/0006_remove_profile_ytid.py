# Generated by Django 3.0.4 on 2020-03-27 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0005_merge_20200327_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ytid',
        ),
    ]
