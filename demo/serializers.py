from django.contrib.auth.models import User
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Question

    
class UserNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name']
        
        
class QuestionListSerializer(serializers.ModelSerializer):
    
    author = UserNestedSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text', 'author']


class QuestionDetailsSerializer(serializers.ModelSerializer):
    
    author = UserNestedSerializer()
    
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text', 'author']
        
    def validate_author(self, data):
        print(data)
        author_id = data.get('id')
        if not User.objects.filter(pk=author_id).exists():
            raise serializers.ValidationError({'author': 'wrong id'})
        return data
    
    def update(self, instance, validated_data):
        if 'author' in validated_data:
            author_id = validated_data.get('author', {}).get('id')
            author = get_object_or_404(User, pk=author_id)
            validated_data['author'] = author
        return super().update(instance, validated_data)
