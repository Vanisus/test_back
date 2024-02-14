from django import template
from django.urls import reverse
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    all_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').order_by('id')
    menu_items = build_tree(all_items)
    return {'menu_items': menu_items}



def build_tree(items):
    tree = []
    for item in items:
        if item.parent is None:
            tree.append(build_node(item, items))
    return tree


def build_node(item, items):
    children = [build_node(child, items) for child in items if child.parent_id == item.id]
    return {
        'name': item.name,
        'url': item.url,
        'named_url': item.named_url,
        'children': children
    }

