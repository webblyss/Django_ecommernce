# Generated by Django 4.0.6 on 2022-07-31 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0004_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='small_image_1',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='small_image_2',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='small_image_3',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
