# Generated by Django 3.2.12 on 2022-03-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IWD_Homes', '0006_host_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
