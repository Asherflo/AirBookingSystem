# Generated by Django 4.1.2 on 2022-10-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlineBooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(auto_now=True),
        ),
    ]
