# Generated by Django 4.0 on 2022-08-02 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0006_defaulter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaulter',
            old_name='batch',
            new_name='defaulter_list',
        ),
        migrations.RemoveField(
            model_name='defaulter',
            name='subtype',
        ),
    ]
