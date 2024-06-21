from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    """
    The table booking model
    """

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
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
    )
    
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.TextField(choices=HOURS, default="13:00")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_user")
    status = models.CharField(choices=STATUS, default='Pending')
    guests = models.SmallIntegerField()
    message = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    changed_fields = []

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = Booking.objects.get(pk=self.pk)
            self.changed_fields = []
            for field in self._meta.fields:
                field_name = field.name
                old_value = getattr(old_instance, field_name)
                new_value = getattr(self, field_name)
                if old_value != new_value:
                    self.changed_fields.append(field_name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-requested_date","requested_time"]

    def __str__(self):
        return f"{self.requested_date} {self.requested_time} - {self.user.first_name} {self.user.last_name}"
    