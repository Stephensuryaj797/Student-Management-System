# Generated by Django 5.0.3 on 2024-03-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0006_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
