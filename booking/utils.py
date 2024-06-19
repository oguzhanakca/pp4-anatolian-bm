from django.core.mail import send_mail
from django.template import Context, Template
from django.conf import settings

# Send email after successful booking
def send_booking_success_email(user, booking):
    subject = 'Booking Successful - Awaiting Confirmation'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email

    with open('booking/templates/booking/email/booking_success.txt') as f:
        template_content = f.read()

    template = Template(template_content)
    context = Context({'user': user, 'booking': booking})
    message = template.render(context)
    send_mail(subject, message, from_email, [to_email])