# Generated by Django 5.1.1 on 2024-10-18 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aot1', '0010_publisher_bookm'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('cat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employ',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('cata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aot1.category')),
            ],
        ),
    ]
