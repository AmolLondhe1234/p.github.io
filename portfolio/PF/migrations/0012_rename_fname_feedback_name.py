# Generated by Django 4.1.5 on 2023-01-25 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PF', '0011_alter_certificate_cert_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='fname',
            new_name='name',
        ),
    ]
