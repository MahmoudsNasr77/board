# Generated by Django 4.1.1 on 2022-09-17 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_courses_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='courses',
        ),
    ]
