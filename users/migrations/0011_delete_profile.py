# Generated by Django 4.0.6 on 2022-08-02 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_delete_store'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]