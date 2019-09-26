# Generated by Django 2.2.5 on 2019-09-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0005_auto_20190925_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='birth_place',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='email',
            field=models.EmailField(blank=True, default='-', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='nik',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='phone_number',
            field=models.CharField(blank=True, default='-', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='school',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
    ]
