from .models import FaceDetection
from rest_framework import serializers


class FaceDetectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaceDetection
        fields = ('image', 'rects')

    def create(self, validated_data):
        data = validated_data['rects']
        rects_data = data.split(', ')

        rects = []

        for rect_data in rects_data:
            temp = rect_data
            temp = temp.replace('[', '', 1)
            temp = temp.replace(']', '', 1)
            rect = temp.split(',')
            rects.append(rect)
        print(rects)
        face_detection = FaceDetection()
        face_detection.rects = rects
        face_detection.image = validated_data['image']

        face_detection.save()

        return face_detection
