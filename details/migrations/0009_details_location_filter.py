# Generated by Django 3.2.18 on 2023-03-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_remove_details_location_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='location_filter',
            field=models.CharField(choices=[('temple_bar', 'Temple Bar'), ('sandymount', 'Sandymount'), ('rathmines', 'Rathmines'), ('portobello', 'Portobello'), ('ballsbridge', 'Ballsbridge'), ('dublin_docklands', 'Dublin Docklands'), ('smithfield', 'Smithfield'), ('cabra', 'Cabra'), ('ashtown', 'Ashtown'), ('phibsborough', 'Phibsborough')], default='normal', max_length=32),
        ),
    ]