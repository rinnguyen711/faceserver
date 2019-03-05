from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FaceDetectionSerializer
from .models import FaceDetection
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect
from MyServer2 import settings

class FaceDetectionViewSet(viewsets.ModelViewSet):
    queryset = FaceDetection.objects.all()
    serializer_class = FaceDetectionSerializer

    @action(methods=['post'], detail=False)
    def new(self, request):
        serializer = FaceDetectionSerializer.create(self, request.data)

        return JsonResponse({'message' : 'SUCCESS'}, status=201)

def index(request):
        db = settings.DATABASES['default']
        print(db['NAME'])
        #return redirect('/api/')

        return HttpResponse(db['NAME'])

    
