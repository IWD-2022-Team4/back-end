# Generated by Django 3.2.12 on 2022-03-05 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IWD_Homes', '0005_auto_20220305_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='available',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
