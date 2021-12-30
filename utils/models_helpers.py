def update_attrs(instance, **attrs):
    """ Update attributes of given model """
    changed = False
    for key, value in attrs.items():
        if getattr(instance, key) != value:
            changed = True
            setattr(instance, key, value)
    return changed


def reload(instance):
    """ Return model instance with forced retrieve from database """
    return instance.__class__.objects.get(pk=instance.pk)


def attr_changed(prev, curr, attr_name):
    """ Check if given attribute changed """
    if not any([prev, curr]):
        return False

    if not all([prev, curr]):
        return True

    return getattr(prev, attr_name) != getattr(curr, attr_name)


