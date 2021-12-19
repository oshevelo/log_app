def enumeration_class_items(class_):
    for name, val in class_.__dict__.items():
        if not name.startswith('_'):
            yield name, val


def is_inside_enumeration_class(string, class_):
    """ Check if given string value is in given class keys """
    for name, val in enumeration_class_items(class_):
        if val == string:
            return True

    return False


def enumeration_class_values(class_):
    """ Return list of values enumerated in class """
    return [value for key, value in enumeration_class_items(class_)]
