# Generated by Django 3.2 on 2021-05-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_userprofile_product_favorites'),
    ]

    operations = [
        migrations.DeleteModel(
            name='commande',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(to='store.Produit'),
        ),
    ]
