# Generated by Django 3.1.7 on 2021-12-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211214_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='bid_winner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
