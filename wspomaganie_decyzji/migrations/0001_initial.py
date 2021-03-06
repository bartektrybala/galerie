# Generated by Django 3.1.1 on 2021-04-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('wielkosc_obiektu', models.CharField(choices=[('1', 'Bardzo mały'), ('2', 'Mały'), ('3', 'Średni'), ('4', 'Dość duży'), ('5', 'Duży'), ('6', 'Ogromny')], max_length=50)),
                ('wiek_obiektu', models.CharField(choices=[('1', 'Bardzo Stary'), ('2', 'Stary+'), ('3', 'Średni'), ('4', 'Nowy'), ('5', 'Dopiero zbudowany (>rok)')], max_length=50)),
                ('obecnosc_hipermarketu', models.BooleanField()),
                ('kino', models.BooleanField()),
                ('kregielnia', models.BooleanField()),
                ('strefa_dla_dzieci', models.BooleanField()),
                ('przestrzen_gastronomiczna', models.BooleanField(choices=[('1', 'Dobrze'), ('2', 'Dobrze+'), ('3', 'Dobrze++'), ('4', 'Źle'), ('5', 'Źle-'), ('6', 'Źle--')], max_length=50)),
                ('strefa_wizualna', models.CharField(choices=[('1', 'Dobrze'), ('2', 'Dobrze+'), ('3', 'Dobrze++'), ('4', 'Źle'), ('5', 'Źle-'), ('6', 'Źle--')], max_length=50)),
                ('fryzjer', models.BooleanField()),
                ('bankomat', models.BooleanField()),
                ('bank', models.BooleanField()),
                ('operator_komorkowy', models.BooleanField()),
                ('lokalizacja', models.TextField()),
            ],
        ),
    ]
