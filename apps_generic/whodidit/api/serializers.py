from rest_framework import serializers

#from apps.users.api.fields import UserField


class WhoDidItBaseSerializer(serializers.Serializer):
    pass
    #created_by = UserField(read_only=True)
    #updated_by = UserField(read_only=True)
