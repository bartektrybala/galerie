# Generated by Django 3.1.1 on 2021-04-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wspomaganie_decyzji', '0004_auto_20210420_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=6)),
            ],
        ),
    ]
