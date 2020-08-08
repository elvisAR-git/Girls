# Generated by Django 3.0.9 on 2020-08-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_admins_quotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_1', models.CharField(max_length=16)),
                ('phone_2', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_1', models.IntegerField(null=True)),
                ('stat_2', models.IntegerField(null=True)),
                ('stat_3', models.IntegerField(null=True)),
            ],
        ),
    ]
