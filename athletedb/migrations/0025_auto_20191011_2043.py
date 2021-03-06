# Generated by Django 2.2.5 on 2019-10-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0024_auto_20191011_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='alamat'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='birth_place',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='tempat lahir'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='umur'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='school',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='sekolah'),
        ),
    ]
