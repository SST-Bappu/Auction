# Generated by Django 3.1.7 on 2021-12-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211213_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
