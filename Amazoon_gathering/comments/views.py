from django.shortcuts import render
from  rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
from .models import *
from .serializers import *
class Linkviewset(viewsets.ModelViewSet):
    queryset =Link.objects.all()
    serializer_class =Link_serial
    http_method_names = ['get','post','put','delete']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(f'hi here {serializer.data}')
        a=serializer.data
        a['state']=1
        print(f'hi here2 {a}')
        serializer2 = self.get_serializer(data=a)
        serializer2.is_valid(raise_exception=True)
        serializer2.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
class Commentviewset(viewsets.ModelViewSet):
    queryset =Comment.objects.all()
    serializer_class =Comment_serial
    http_method_names = ['get','post','put','delete']