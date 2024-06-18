from django.db import models
from django.contrib.auth.models import User


# Booking status
STATUS = (
    ('Awaiting confirmation', 'Awaiting confirmation'),
    ('Confirmed', 'Confirmed'),
    ('Rejected', 'Rejected'),
    ('Cancelled', 'Cancelled'),
    ('Expired', 'Expired'),
)

# Create your models here.

class Booking(models.Model):
    """
    The table booking model
    """
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.TimeField(help_text="Available between 13:00 - 23:00")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_user")
    status = models.CharField(choices=STATUS, default='Awaiting confirmation')
    guests = models.SmallIntegerField()
    message = models.TextField(blank=True)

    class Meta:
        ordering = ["-requested_date","requested_time"]

    def __str__(self):
        return f"{self.requested_date} {self.requested_time} - {self.user.first_name} {self.user.last_name}"
    