# Generated by Django 3.0.6 on 2020-08-01 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imgapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='added_date',
        ),
    ]
