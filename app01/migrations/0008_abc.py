# Generated by Django 4.1.3 on 2023-02-01 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ad_product')),
            ],
        ),
    ]