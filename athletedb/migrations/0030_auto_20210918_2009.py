# Generated by Django 2.2.13 on 2021-09-18 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0029_auto_20200119_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievementlist',
            options={'verbose_name': 'Perolehan Medali', 'verbose_name_plural': 'Perolehan Medali'},
        ),
        migrations.AlterModelOptions(
            name='achievementmapping',
            options={'verbose_name': 'Medali Prestasi', 'verbose_name_plural': 'Medali Prestasi'},
        ),
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ['-id'], 'verbose_name': 'Atlet', 'verbose_name_plural': 'Atlet'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Olimpiade', 'verbose_name_plural': 'Olimpiade'},
        ),
        migrations.AlterModelTable(
            name='achievement',
            table='public.athletedb_achievement',
        ),
        migrations.AlterModelTable(
            name='achievementlist',
            table='public.athletedb_achievementlist',
        ),
        migrations.AlterModelTable(
            name='achievementmapping',
            table='public.athletedb_achievementmapping',
        ),
        migrations.AlterModelTable(
            name='athlete',
            table='public.athletedb_athlete',
        ),
        migrations.AlterModelTable(
            name='event',
            table='public.athletedb_event',
        ),
        migrations.AlterModelTable(
            name='sport',
            table='public.athletedb_sport',
        ),
        migrations.CreateModel(
            name='AthleteSports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athletes_athletesports', to='athletedb.Athlete')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sports_athletesports', to='athletedb.Sport')),
            ],
            options={
                'verbose_name': 'Olahraga atlit',
                'verbose_name_plural': 'Olahraga atlit',
                'db_table': 'public.athletedb_athletesports',
            },
        ),
    ]
