# Generated by Django 4.0.6 on 2022-08-02 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_store_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Store',
        ),
    ]
