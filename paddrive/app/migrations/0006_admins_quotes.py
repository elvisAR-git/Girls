# Generated by Django 3.0.9 on 2020-08-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_socialevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('position', models.CharField(blank=True, max_length=40, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('web_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('position', models.CharField(blank=True, max_length=40, null=True)),
                ('quote', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
