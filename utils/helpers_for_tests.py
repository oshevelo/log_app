import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


from utils.enum_class import is_inside_enumeration_class
from utils.models_helpers import update_attrs
#from apps.auth.models import UserProfile


def create_user(username, user_kwargs_dict=None, profile_kwargs_dict=None):
    user_kwargs_dict = user_kwargs_dict or dict()
    profile_kwargs_dict = profile_kwargs_dict or dict()

    user_kw = dict(
        username=username,
        password='111',
        email=username + '.com'
    )
    user_kw.update(user_kwargs_dict)
    user_kw['password'] = make_password(user_kw['password'])
    user = User.objects.create(**user_kw)

    profile_kw = dict(
        user=user,
        phone='0932308250'
    )
    profile_kw.update(profile_kwargs_dict)
    #UserProfile.objects.create(**profile_kw)

    return user


def login_user(client, user, password='111'):
    client.login(username=user.username, password=password)


def _dict_key_quotes(text):
    """ Replaces first two occurrences of double quotes " to single quotes ' in every line

        Is used to print dictionaries formatted according to the project guidelines
        (dict key are in single quotes, texts are in double quotes)
    """
    return '\n'.join([l.replace('"', "'", 2) for l in text.split('\n')])


def dump(response):
    """ Print DRF response data

        Useful for debugging tests. Prints response code and indented JSON data

    :param response: server response provided by DRF testing client (APIClient)
    """

    print("\nURL:", response.request['PATH_INFO'])
    print("Method:", response.request['REQUEST_METHOD'])
    if response.request['QUERY_STRING']:
        print("Query:", response.request['QUERY_STRING'])
    print("\n")
    print("Status code:\n{}\n\nData:\n{}\n".format(
        response.status_code,
        _dict_key_quotes(json.dumps(response.data, indent=4, ensure_ascii=False))
        if hasattr(response, 'data') else None
    ))


def dump_record(metric_record):
    """ Print metric record info """
    try:
        print(
            "{r.metric.__class__.__name__}: {r.metric.abbr}\n"
            "value:      {r.value}\n"
            "applicable: {r.applicable}\n".format(r=metric_record)
        )
        if hasattr(metric_record, 'calc_error'):
            print(
                "error:     {r.calc_error}\n"
                "warning:   {r.calc_warning}\n".format(r=metric_record)
            )
    except Exception as e:
        print("Error in dump_record:", str(e))
        raise e


def s_uuid(obj):
    assert hasattr(obj, 'uuid')
    return str(obj.uuid)
