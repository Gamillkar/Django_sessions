# Generated by Django 3.1.1 on 2020-10-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergameinfo',
            name='gameover',
        ),
        migrations.AddField(
            model_name='playergameinfo',
            name='success_attempt',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
