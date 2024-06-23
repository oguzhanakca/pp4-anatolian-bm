from django import template

register = template.Library()

# All of blog url tags

@register.simple_tag(takes_context=True)
def blog_urls(context):
    request= context["request"]
    blog_url_pattern = '/blog/'
    return request.path.startswith(blog_url_pattern)