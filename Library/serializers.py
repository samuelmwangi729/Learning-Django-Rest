from rest_framework import serializers
from Institutions.models import Institution
from Library.models import Books,Author
from Account.models import User
class BookSerializer(serializers.ModelSerializer):
    authors = serializers.CharField(write_only=True)
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Books
        fields  = '__all__'

    def validate(self,attrs):
        username = attrs.get('authors')
        try:
            user = Author.objects.get(name=username)
        except Author.DoesNotExist:
            raise serializers.ValidationError({
                "user":"author does not exist"
                })
        attrs['author'] = user
        return attrs
    def create(self,validated_data):
        validated_data.pop('authors')
        book = Books.objects.create(**validated_data)
        return book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields=['name','title','bio']
        
    def validate(self,data):
        author_name = data.get('name')
        if self.instance:
            if self.instance.name ==author_name:
                return data
        if Author.objects.filter(name=author_name).exists():
            raise serializers.ValidationError({"author":"the author already exists"})
        return data
    
    def create(self,validated_data):
        return Author.objects.create(**validated_data)