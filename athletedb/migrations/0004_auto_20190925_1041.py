# Generated by Django 2.2.5 on 2019-09-25 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletedb', '0003_auto_20190925_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='achievements',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='participated_in',
        ),
        migrations.CreateModel(
            name='AchievementMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='athletedb.AchievementList')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athletes', to='athletedb.Athlete')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='athletedb.Event')),
            ],
        ),
    ]