# Generated by Django 3.0.5 on 2024-05-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0007_worker_buyeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicebook',
            name='buyerphone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
