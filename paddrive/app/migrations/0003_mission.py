# Generated by Django 3.0.9 on 2020-08-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200804_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_statement', models.CharField(blank=True, max_length=100, null=True)),
                ('mission_description', models.TextField()),
                ('img_1', models.ImageField(null=True, upload_to='')),
                ('img_2', models.ImageField(null=True, upload_to='')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
