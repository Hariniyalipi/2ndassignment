# Generated by Django 5.0.6 on 2024-06-13 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=30)),
                ('lName', models.CharField(max_length=30)),
                ('Aadhaar', models.CharField(max_length=12, unique=True)),
                ('Pincode', models.CharField(max_length=6)),
                ('CustomerId', models.CharField(editable=False, max_length=10)),
            ],
        ),
    ]
