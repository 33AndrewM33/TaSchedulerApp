# Generated by Django 5.1.2 on 2024-11-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAScheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]