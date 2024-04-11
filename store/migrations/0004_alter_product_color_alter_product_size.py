# Generated by Django 5.0.4 on 2024-04-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, to='store.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='store.size'),
        ),
    ]
