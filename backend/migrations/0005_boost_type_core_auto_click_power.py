# Generated by Django 4.0.3 on 2022-06-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_boost_level_alter_core_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'auto'), (0, 'casual')], default=0),
        ),
        migrations.AddField(
            model_name='core',
            name='auto_click_power',
            field=models.IntegerField(default=0),
        ),
    ]
