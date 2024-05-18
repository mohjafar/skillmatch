# Generated by Django 3.0.5 on 2024-05-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0011_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicebook',
            name='is_cancell',
        ),
        migrations.AddField(
            model_name='servicebook',
            name='cancell',
            field=models.IntegerField(choices=[(0, 'Panding'), (1, 'Complete')], default=1),
        ),
    ]
