from .models import FaceDetection
from rest_framework import serializers
import requests


class FaceDetectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaceDetection
        fields = ('image', 'rects')

    def create(self, validated_data):
        face_detection = FaceDetection()
        image = validated_data['image']

        if 'rects' in validated_data:
            data = validated_data['rects']

            rects_data = data.split(', ')

            rects = []
            count = len(rects_data)
            #print(rects_data)
            #print(count)
            if count != 0:
                for rect_data in rects_data:
                    #print(rect_data)
                    temp = rect_data
                    temp = temp.replace('[', '', 1)
                    temp = temp.replace(']', '', 1)
                    rect = temp.split(',')
                    rects.append(rect)
            #print(rects)
            leng = len(rects)
            face_detection.rects = rects
        else:
            face_detection.rects = []

        face_detection.image = validated_data['image']
        face_detection.save()
        
        
        files = {'image': open(face_detection.image.path, 'rb')}
        response = requests.post(url='http://rinnguyen.pythonanywhere.com/api/faces/new/', files=files)
        content = response.content

        return face_detection
