# Generated by Django 2.2.5 on 2019-10-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0020_auto_20191008_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='kk',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/kartu-keluarga/', verbose_name='Foto Kartu Keluarga'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/kartu-keluarga/', verbose_name='Pasfoto'),
        ),
    ]