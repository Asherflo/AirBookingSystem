# Generated by Django 4.1.2 on 2022-10-13 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(choices=[('F', 'First_class'), ('B', 'Business'), ('C', 'Economic')], default='B', max_length=1)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phoneNumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=45)),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('zip', models.PositiveIntegerField(null=True)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='airlineBooking.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('E', 'Economic'), ('B', 'Business'), ('F', 'First_class')], default='B', max_length=1)),
                ('ticket_date', models.DateField(auto_now_add=True)),
                ('ticket_description', models.CharField(max_length=255)),
                ('ticket_booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airlineBooking.booking')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airlineBooking.passenger'),
        ),
    ]
