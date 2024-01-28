# Generated by Django 5.0.1 on 2024-01-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restorant', '0004_remove_restaurant_qr_code_remove_restaurant_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='restaurant_qr_codes/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
