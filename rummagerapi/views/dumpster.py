'''View module for handling requests about dumpsters'''
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rummagerapi.models import Dumpster

class DumpsterView(ViewSet):
    '''Rummager Dumpsters'''

    #Creation for Dumpster is handled within Haul ViewSet

    def retrieve(self, request, pk=None):
        '''Handles GET request for single dumpster'''

        try:
            dumpster = Dumpster.objects.get(pk=pk)
            serializer = DumpsterSerializer(dumpster, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        '''Handles GET request for all dumpsters'''

        dumpsters = Dumpster.objects.all()

        serializer = DumpsterSerializer(
            dumpsters, many=True, context={'request': request}
        )
        return Response(serializer.data)


class DumpsterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dumpster
        fields = ('id', 'location')
        depth = 1