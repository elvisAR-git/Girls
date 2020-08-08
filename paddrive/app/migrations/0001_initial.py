# Generated by Django 3.0.9 on 2020-08-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hq_image', models.ImageField(null=True, upload_to='bestblog/images/')),
                ('main_title', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HomepageSlides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hq_image', models.ImageField(null=True, upload_to='slides')),
                ('main_title', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField()),
            ],
        ),
    ]