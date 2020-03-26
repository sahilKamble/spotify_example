# Generated by Django 3.0.4 on 2020-03-26 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0002_profile_gcreds'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='spid',
            field=models.CharField(max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ytid',
            field=models.CharField(max_length=99, null=True),
        ),
        migrations.CreateModel(
            name='YtTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vidid', models.CharField(max_length=99, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spot.Profile')),
            ],
        ),
    ]
