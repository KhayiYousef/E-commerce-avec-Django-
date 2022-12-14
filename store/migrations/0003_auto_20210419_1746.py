# Generated by Django 3.2 on 2021-04-19 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_produit_prix'),
    ]

    operations = [
        migrations.CreateModel(
            name='produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('public_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='produit',
            name='prix',
        ),
    ]
