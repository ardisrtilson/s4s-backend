from s4sbackendapi.models.s4sUser import s4sUser
from django import utils
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from s4sbackendapi.models import Samples as SamplesModel
from django.contrib.auth.models import User

class Samples(ViewSet):

    def create(self, request):

        user = s4sUser.objects.get(user=request.auth.user)
        sample = SamplesModel()
        sample.user = user
        try:
            sample.audio_url = request.data["audio_url"]
            sample.color = request.data["color"]
            sample.rating = request.data["rating"]
            sample.date_added = request.data["date_added"]
            sample.loudness = request.data["loudness"]
            sample.name = request.data["name"]
            sample.uploader = user
        except KeyError as ex:
            return Response({'Reason'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            sample.save()
            serializer = SampleSerializer(sample, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = s4sUser
        fields = ('user', 'sex')

class SampleSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    user=UserSerializer(many=False)
    class Meta:
        model = SamplesModel
        fields = ('audio_url', 'color', 'date_added', 'loudness', 'name', 'uploader', 'user')