# Generated by Django 4.1.4 on 2023-03-28 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_remove_person_city_remove_person_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='email',
            new_name='mail_id',
        ),
    ]