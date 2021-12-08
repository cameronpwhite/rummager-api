'''View module for handling requests about hauls'''
from rummagerapi.views.dumpster import DumpsterSerializer
from rummagerapi.views.tag import TagSerializer
from rummagerapi.views.item import ItemSerializer
from rummagerapi.models.haul import Haul
from rummagerapi.models.diver import Diver
from rummagerapi.models.item import Item
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rummagerapi.models import Dumpster, Item, Tag, dumpster

class HaulView(ViewSet):
    '''Rummager Hauls'''

    def create(self, request):
        '''Handle POST request'''


        #Get user for assigning to Haul
        diver = Diver.objects.get(user=request.auth.user)

        #Create python instance of a Haul class and set
        #properties from the request body from client.

        haul = Haul()
        haul.description = request.data['description']
        haul.image_path = request.data['image_path']
        haul.diver = diver

        #Gets a dumpster that is already in the database if request's location property is the same,
        #if it is a new request, the dumpster is created in the database.
        #Then it is assigned to the dumpster.
        dumpster, created = Dumpster.objects.get_or_create(
            location = request.data['dumpster']
        )
        haul.dumpster = dumpster

        try:
            haul.save()
            #Filter tags by the tags in the request data
            #Assigns tags to haul with set method
            haul.tags.set(request.data['tags'])
            #Gets items from the request.
            items = request.data['items']
            #Loops through the items from request and assigns them to the Haul that was just created.
            for item in items:
                Item.objects.create(haul=Haul.objects.last(), name=item)
            serializer = HaulSerializer(haul, context={'request':request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''Handles GET request for singular Haul'''
        try:
            haul = Haul.objects.get(pk=pk)
            serializer = HaulSerializer(haul, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        '''Handles PUT request for a Haul'''

        diver = Diver.objects.get(user=request.auth.user)
        
        haul = Haul.objects.get(pk=pk)
        haul.description = request.data['description']
        haul.image_path = request.data['image_path']
        haul.diver = diver
        dumpster, created = Dumpster.objects.get_or_create(
            location = request.data['dumpster']
        )
        haul.dumpster = dumpster
        haul.tags = request.data['tags']
        haul.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        '''Handle DELETE requests for a single Haul'''

        try:
            haul = Haul.objects.get(pk=pk)
            haul.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Haul.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        '''Handles GET request to Hauls resource'''

        hauls = Haul.objects.all()

        serializer = HaulSerializer(
            hauls, many=True, context={'request': request}
        )

        return Response(serializer.data)


    #Use @api_view for making custom actions



#Q: Do I have to create HaulTags and HaulItem Serializers in order to display them properly?
class HaulTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'label']

class HaulItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']

class HaulDumpsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dumpster
        fields = ['id', 'location']

class HaulUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name']

class HaulDiverSerializer(serializers.ModelSerializer):
    
    user = HaulUserSerializer(many=False)

    class Meta:
        model = Diver
        fields = ['user']

class HaulSerializer(serializers.ModelSerializer):
    dumpster = HaulDumpsterSerializer(many=False)
    tags = HaulTagSerializer(many=True)
    items = HaulItemSerializer(many=True)
    diver = HaulDiverSerializer(many=False)
    
    class Meta:
        model = Haul
        fields = ('id','description', 'image_path', 'diver', 'dumpster', 'tags', 'items')
        depth = 1


