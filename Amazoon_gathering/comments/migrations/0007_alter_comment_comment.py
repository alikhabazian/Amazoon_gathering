# Generated by Django 4.0.6 on 2022-07-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_alter_comment_comment_alter_link_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=10000),
        ),
    ]
