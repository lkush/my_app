# Generated by Django 3.0.3 on 2020-02-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sampleinfo',
            fields=[
                ('sampleid', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('archperiod', models.CharField(max_length=100)),
                ('archculture', models.CharField(max_length=200)),
                ('archdate', models.CharField(max_length=100)),
                ('archsite', models.CharField(max_length=100)),
                ('geopoint', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8)),
                ('long', models.DecimalField(decimal_places=6, max_digits=8)),
                ('geneticsex', models.CharField(max_length=100)),
                ('mtdnahg', models.CharField(max_length=100)),
                ('ychrhg', models.CharField(max_length=100)),
                ('wgsdata', models.CharField(max_length=200)),
            ],
        ),
    ]