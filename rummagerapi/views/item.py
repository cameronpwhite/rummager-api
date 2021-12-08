from django.core.exceptions import ValidationError
from rummagerapi.models.haul import Haul
from django.db import models
from django.http import HttpResponseServerError
from rest_framework.viewsets import  ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rummagerapi.models.item import Item

class ItemView(ViewSet):
    '''Rummager haul items'''

    #Creation for Item is handled within Haul ViewSet

    def retrieve(self, request, pk=None):
        '''Handle GET requests for a single item.
        
            Returns - Response: JSON Serialized Item'''

        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        '''GET requests for all items'''

        items = Item.objects.all()
        serializer = ItemSerializer(
            items, many=True, context={'request': request}
        )
        return Response(serializer.data)



class ItemSerializer(serializers.ModelSerializer):
    '''JSON Serializer for items'''

    class Meta:
        model = Item
        fields = ('id', 'name', 'haul')
        depth = 1