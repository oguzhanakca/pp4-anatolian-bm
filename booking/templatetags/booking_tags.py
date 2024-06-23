from django import template

register = template.Library()

# All of booking url tags

@register.simple_tag(takes_context=True)
def booking_urls(context):
    request= context["request"]
    booking_url_pattern = '/booking/'
    return request.path.startswith(booking_url_pattern)