# Generated by Django 3.2.12 on 2022-03-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IWD_Homes', '0011_auto_20220306_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='family_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='family_number',
            field=models.IntegerField(default=1),
        ),
    ]
