# Generated by Django 3.0.9 on 2020-08-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200806_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='stat_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='stat_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='stat_3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
