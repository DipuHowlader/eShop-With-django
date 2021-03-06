# Generated by Django 3.2.5 on 2021-07-28 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20210728_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
