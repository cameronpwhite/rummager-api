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

    def update(self, request, pk=None):
        '''Handle PUT requests for a single Item'''

        item = Item.objects.get(pk=pk)
        item.name = request.data['name']
        item.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
        

    def destroy(self, request, pk=None):
        '''Handle DELETE requests for a single Item'''

        try:
            item = Item.objects.get(pk=pk)
            item.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Haul.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ItemSerializer(serializers.ModelSerializer):
    '''JSON Serializer for items'''

    class Meta:
        model = Item
        fields = ('id', 'name', 'haul')