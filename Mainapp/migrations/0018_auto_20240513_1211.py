# Generated by Django 3.0.5 on 2024-05-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0017_auto_20240509_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicebook',
            name='service',
        ),
        migrations.AddField(
            model_name='servicebook',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, to='Mainapp.Buyer'),
        ),
    ]
