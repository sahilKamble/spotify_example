# Generated by Django 3.0.4 on 2020-03-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0006_remove_profile_ytid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ytid',
            field=models.CharField(max_length=99, null=True),
        ),
    ]