# Generated by Django 3.1.1 on 2021-04-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wspomaganie_decyzji', '0002_auto_20210413_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='image',
            field=models.ImageField(blank=True, default='default-image.png', null=True, upload_to='wspomaganie_decyzji/'),
        ),
    ]
