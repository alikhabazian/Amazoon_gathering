# Generated by Django 4.0.6 on 2022-07-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='state',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
