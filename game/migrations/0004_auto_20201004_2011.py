# Generated by Django 3.1.1 on 2020-10-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20201004_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='success_attempt',
            field=models.IntegerField(null=True),
        ),
    ]