from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FaceDetectionSerializer
from .models import FaceDetection
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http.response import JsonResponse


class FaceDetectionViewSet(viewsets.ModelViewSet):
    queryset = FaceDetection.objects.all()
    serializer_class = FaceDetectionSerializer

    @action(methods=['post'], detail=False)
    def new(self, request):
        serializer = FaceDetectionSerializer.create(self, request.data)


        return Response('')

