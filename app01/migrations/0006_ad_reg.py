# Generated by Django 4.1.3 on 2023-01-18 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_ad_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ad_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
