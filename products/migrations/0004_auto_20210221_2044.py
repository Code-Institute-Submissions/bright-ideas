# Generated by Django 3.1.6 on 2021-02-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210220_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='clearance',
            new_name='is_clearance',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='dimmable',
            new_name='is_dimmable',
        ),
        migrations.AddField(
            model_name='product',
            name='is_multipack',
            field=models.BooleanField(default=False),
        ),
    ]
