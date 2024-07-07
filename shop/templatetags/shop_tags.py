from django import template

register = template.Library()

# All of shop url tags

@register.simple_tag(takes_context=True)
def shop_urls(context):
    request= context["request"]
    shop_url_pattern = '/shop/'
    return request.path.startswith(shop_url_pattern)