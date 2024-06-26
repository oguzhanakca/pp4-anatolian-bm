# Generated by Django 4.2.13 on 2024-06-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_message_alter_booking_requested_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='requested_time',
            field=models.TextField(choices=[('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], default='13:00'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Awaiting', 'Awaiting'), ('Confirmed', 'Confirmed'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled'), ('Expired', 'Expired')], default='Awaiting confirmation'),
        ),
    ]
