# Generated by Django 3.0.5 on 2020-04-26 21:23

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200424_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]