from django.core.mail import send_mail
from django.template import Context, Template
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Booking


@receiver(post_save, sender=Booking)
def send_booking_status_email(sender, instance, **kwargs):
    if 'status' in instance.changed_fields:
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = f"Booking Status Changed"
        f_path = 'booking/templates/booking/email/booking_status_changed.txt'
        with open(f_path) as f:
            template_content = f.read()
        template = Template(template_content)
        context = Context({'user': instance.user, 'booking': instance})
        message = template.render(context)
        to_email = [instance.user.email]
        send_mail(subject, message, from_email, to_email)
