# Generated by Django 4.1.3 on 2023-02-02 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_abc'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.u_reg')),
            ],
        ),
    ]
