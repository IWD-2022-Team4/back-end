from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User, Host
from .serializers import *

from django.forms.models import model_to_dict
from django.contrib.auth.models import User as U


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        data = User.objects.all()

        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def host_list(request):
    if request.method == 'GET':
        data = Host.objects.all()

        serializer = HostSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def change_data(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def matches(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    hosts = Host.objects.all()
    host_serializer = HostSerializer(hosts, context={'request': request}, many=True)
    list_of_home_matches = []

    for data in host_serializer.data: 
        if user.disability == data['disability']: 
            list_of_home_matches.append(data)

    matches_serializer = HostSerializer(list_of_home_matches, context={'request':request}, many=True)
    return Response(matches_serializer.data)


