# Generated by Django 3.2.12 on 2022-03-05 18:02

from django.db import migrations

def create_data(apps, schema_editor):
    User = apps.get_model('IWD_Homes', 'User')
    User(name="Joe Silver", email="joe@email.com", city="London", phone="00000000").save()


class Migration(migrations.Migration):

    dependencies = [
        ('IWD_Homes', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_data),
    ]
