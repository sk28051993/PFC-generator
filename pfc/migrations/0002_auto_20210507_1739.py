# Generated by Django 3.2.2 on 2021-05-07 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pfc',
            name='pfc_name',
        ),
        migrations.AddField(
            model_name='pfc',
            name='Year_to_be_forward',
            field=models.IntegerField(default=2017),
        ),
    ]