# Generated by Django 3.1.1 on 2020-10-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20201004_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergameinfo',
            name='success_attempt',
        ),
        migrations.AddField(
            model_name='player',
            name='success_attempt',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
