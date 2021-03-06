# Generated by Django 2.2.4 on 2019-08-28 17:49

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('bidi', models.BooleanField()),
                ('name', models.CharField(max_length=50)),
                ('name_local', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='providers.Currency')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='providers.Language')),
            ],
        ),
    ]
