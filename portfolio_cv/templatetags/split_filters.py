from django import template

register = template.Library()

@register.filter(name='split')
def split(value, sep=','):
    """Split a string by `sep` and return list of trimmed non-empty items.

    Usage in template:
      {% load split_filters %}
      {% for item in value|split:',' %}{{ item }}{% endfor %}
    """
    if value is None:
        return []
    try:
        # Ensure value is a string
        s = str(value)
    except Exception:
        return []
    items = [part.strip() for part in s.split(sep)]
    return [i for i in items if i]
