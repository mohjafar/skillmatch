# Generated by Django 3.0.5 on 2024-05-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0013_remove_servicebook_cancell'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicebook',
            name='cancell',
            field=models.IntegerField(choices=[(0, 'Panding'), (1, 'Complete')], default=0),
        ),
    ]
