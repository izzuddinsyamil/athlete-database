# Generated by Django 2.2.5 on 2019-11-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0027_auto_20191106_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='nomor telepon'),
        ),
    ]
