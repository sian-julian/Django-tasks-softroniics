# Generated by Django 5.1.1 on 2024-10-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aot1', '0005_remove_product_stock_qnty_product_stock_qntuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
