# Generated by Django 5.1.1 on 2024-10-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aot1', '0011_category_employ'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookm',
            old_name='pub_name',
            new_name='Publisher',
        ),
        migrations.RenameField(
            model_name='bookm',
            old_name='publication_date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]