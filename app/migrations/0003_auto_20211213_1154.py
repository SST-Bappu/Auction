# Generated by Django 3.1.7 on 2021-12-13 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_useraccount_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='auctionItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('min_bid', models.FloatField(null=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('end_date', models.DateTimeField(null=True)),
                ('ueser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
