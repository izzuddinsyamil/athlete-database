# Generated by Django 2.2.5 on 2019-10-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0019_athlete_ktp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='ktp',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/ktp/', verbose_name='Foto Ktp'),
        ),
    ]
