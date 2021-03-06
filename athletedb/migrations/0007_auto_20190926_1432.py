# Generated by Django 2.2.5 on 2019-09-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0006_auto_20190926_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='nik',
            field=models.CharField(blank=True, default='-', max_length=255, null=True, unique=True),
        ),
    ]
