# Generated by Django 3.0.5 on 2024-05-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0016_buyer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicebook',
            name='cancell',
            field=models.IntegerField(choices=[(0, 'Panding'), (1, 'Done'), (2, 'Complete')], default=0),
        ),
    ]
