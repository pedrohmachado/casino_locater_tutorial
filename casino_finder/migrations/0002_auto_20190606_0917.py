# Generated by Django 2.2.2 on 2019-06-06 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_finder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casino',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
