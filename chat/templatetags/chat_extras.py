from django import template

register = template.Library()


@register.filter(name='is_friend')
def is_friend(user, user_id):
    control = user.profile.friends.filter(id=user_id).exists()
    return control
