# Generated by Django 5.0.3 on 2024-03-30 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0011_assessment_users_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='user_score',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='users',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='users_completed',
        ),
    ]
