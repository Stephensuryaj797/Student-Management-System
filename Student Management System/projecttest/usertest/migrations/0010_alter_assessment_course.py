# Generated by Django 5.0.3 on 2024-03-30 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0009_assessment_users_course_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='usertest.course'),
        ),
    ]
