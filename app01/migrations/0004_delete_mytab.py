# Generated by Django 4.1.3 on 2023-01-09 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_u_reg_delete_cont_tb_rename_fname_mytab_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mytab',
        ),
    ]
