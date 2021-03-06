# Generated by Django 3.0.4 on 2020-04-01 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0011_auto_20200401_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=99, null=True)),
                ('yt_playlistid', models.CharField(max_length=99, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spot.Profile')),
            ],
        ),
    ]
