# Generated by Django 3.0.5 on 2024-04-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
