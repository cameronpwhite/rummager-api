from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rummagerapi.models import Diver

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles authentication of a diver
        
    Method arguments:
        request -- Full HTTP Request object'''
    
    username = request.data['username']
    password = request.data['password']

    #Use authenticate method to verify.

    authenticated_user = authenticate(username=username, password=password)

    #If auth was success, respond with their token

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        #Bad login details were provided, will not log in user
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles creation of new diver for authentication'''

    #Create a new user by invoking 'create_user' method on User model.

    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )

    #Save info into rummagerapi_diver table
    diver = Diver.objects.create(
        user = new_user
    )

    #Generate new token on user account
    token = Token.objects.create(user=diver.user)

    #Return token to the client
    data = { 'token': token.key }
    return Response(data)