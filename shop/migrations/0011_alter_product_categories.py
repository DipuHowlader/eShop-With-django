# Generated by Django 3.2.5 on 2021-07-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('BLUCHER SHOE', 'BLUCHER SHOE'), ('CLOG SHOE', 'CLOG SHOE'), ('SNOW BOOT SHOE', 'SNOW BOOT SHOE'), ('GALESH SHOE', 'GALESH SHOE'), ('PATAUGAS SHOE', 'PATAUGAS SHOE'), ('JAZZ SHOE', 'JAZZ SHOE')], default='BLUCHER SHOE', max_length=50),
        ),
    ]