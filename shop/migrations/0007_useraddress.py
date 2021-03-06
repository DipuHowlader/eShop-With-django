# Generated by Django 3.2.3 on 2021-07-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='userAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=6)),
                ('town', models.CharField(max_length=100)),
                ('address', models.CharField(choices=[('--', '------'), ('of', 'Office'), ('ho', 'Home'), ('co', 'Commercial')], max_length=2)),
            ],
        ),
    ]
