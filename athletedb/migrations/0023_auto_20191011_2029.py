# Generated by Django 2.2.5 on 2019-10-11 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0022_auto_20191010_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='event',
        ),
        migrations.RemoveField(
            model_name='achievement',
            name='position',
        ),
        migrations.RemoveField(
            model_name='achievement',
            name='title',
        ),
        migrations.AddField(
            model_name='achievement',
            name='athlete',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='athlete_achievements', to='athletedb.Athlete'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='certificate_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/sertifikat/', verbose_name='File sertifikat'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='level',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Tingkat kejuaraan'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='result',
            field=models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Hasil'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Deskripsi'),
        ),
    ]
