# Generated by Django 5.0.3 on 2024-03-30 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0012_remove_assessment_user_score_remove_assessment_users_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='thumbnail',
        ),
    ]
