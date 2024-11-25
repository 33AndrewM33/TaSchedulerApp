# Generated by Django 5.1.2 on 2024-11-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAScheduler', '0006_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='instructortocourse',
            constraint=models.UniqueConstraint(fields=('instructor', 'course'), name='unique_instructor_course'),
        ),
    ]
