# Generated by Django 5.1.1 on 2024-10-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aot1', '0007_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]