# Generated by Django 4.0.6 on 2022-07-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_link_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='link',
            name='state',
            field=models.IntegerField(),
        ),
    ]
