# Generated by Django 4.1.5 on 2023-01-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PF', '0009_alter_certificate_cert_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='cert_img',
            field=models.ImageField(upload_to='images2/'),
        ),
    ]
