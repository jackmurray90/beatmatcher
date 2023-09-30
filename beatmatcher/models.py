from django.db import models
from django.contrib.auth.models import User
import re


def is_valid_username(username):
    return (
        re.fullmatch("[a-zA-Z0-9_@+.-]*", username)
        and len(username) > 0
        and len(username) <= 150
    )


class SignUp(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=23)
    expiry = models.DateTimeField()


class Interest(models.Model):
    TYPE_CHOICES = [
        ("dj", "DJ"),
        ("band", "Band"),
        ("act", "Live act"),
        ("venue", "Venue"),
        ("festival", "Festival"),
        ("event", "Event organizer"),
    ]
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class DJ(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.BooleanField()
    booking_url = models.CharField(max_length=200, null=True)
    soundcloud_url = models.CharField(max_length=200)
    rate = models.IntegerField(null=True)


class BookingRequest(models.Model):
    STATES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    arrival_time = models.DateTimeField()
    hours = models.IntegerField()
    other_information = models.TextField()
    rate = models.IntegerField(null=True)
    state = models.CharField(max_length=200, choices=STATES, default="pending")
