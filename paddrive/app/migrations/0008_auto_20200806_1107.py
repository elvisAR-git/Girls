# Generated by Django 3.0.9 on 2020-08-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_contactinformation_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]