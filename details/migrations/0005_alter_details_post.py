# Generated by Django 3.2.18 on 2023-03-04 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('details', '0004_alter_details_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
