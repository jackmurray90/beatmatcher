# Generated by Django 4.2.5 on 2023-09-30 09:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("beatmatcher", "0012_rename_state_booking_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="arrival_time",
            new_name="set_time",
        ),
    ]
