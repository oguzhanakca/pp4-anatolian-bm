from django import template

register = template.Library()

# All of shop url tags

@register.simple_tag(takes_context=True)
def shop_urls(context):
    request= context["request"]
    shop_url_pattern = '/shop/'
    my_cart = '/shop/my_cart/'

    if request.path == my_cart:
        return False
    return request.path.startswith(shop_url_pattern)

# Convert value to int (for filter products)
@register.filter()
def to_int(value):
    return int(value)