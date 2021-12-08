'''View module for handling request about tags'''
from  django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rummagerapi.models import Tag

class TagView(ViewSet):
    '''Rummager haul post tags'''

    def retrieve(self, request, pk=None):
        '''Handle GET requests for single tag

        Returns:
            Response - JSON serialized tag
        '''
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        '''GET Request for all tags
        
        Returns:
            Response - JSON serialized list of tags
        '''
        tags = Tag.objects.all()
        serializer = TagSerializer(
            tags, many=True,context={'request': request})
        return Response(serializer.data)


class TagSerializer(serializers.ModelSerializer):
    '''JSON Serializer for tags'''

    class Meta:
        model = Tag
        fields = ('id', 'label')
        depth = 1
