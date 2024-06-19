from django.db import models
from django.contrib.auth.models import User


# Available hours
HOURS = (
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
    ('23:00', '23:00'),
)

# Booking status
STATUS = (
    ('Awaiting', 'Awaiting'),
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
    requested_time = models.TextField(choices=HOURS, default="13:00")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_user")
    status = models.CharField(choices=STATUS, default='Awaiting')
    guests = models.SmallIntegerField()
    message = models.TextField(blank=True)
    phone = models.TextField(blank=True)

    class Meta:
        ordering = ["-requested_date","requested_time"]

    def __str__(self):
        return f"{self.requested_date} {self.requested_time} - {self.user.first_name} {self.user.last_name}"
    