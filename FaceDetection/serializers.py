from .models import FaceDetection
from rest_framework import serializers
import requests


class FaceDetectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaceDetection
        fields = ('image', 'rects')

    def create(self, validated_data):
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



        face_detection = FaceDetection()
        face_detection.rects = rects
        face_detection.image = validated_data['image']
        if rects[0] == ['']:
            face_detection.rects = []

        face_detection.save()
        post_data = {'image': image}
        response = requests.post(url='http://rinnguyen.pythonanywhere.com/api/faces/new/', data=post_data)
        content = response.content
        print("SEND REQUESTS: ")
        print(content)

        return face_detection
