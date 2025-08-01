# Generated by Django 5.2.4 on 2025-07-24 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'سلة', 'verbose_name_plural': 'السلال'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'عنصر سلة', 'verbose_name_plural': 'عناصر السلة'},
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='storefront.cart', verbose_name='السلة'),
        ),
    ]
