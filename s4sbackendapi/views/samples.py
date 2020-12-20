from django import utils
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from s4sbackendapi.models import Samples as SamplesModel
from django.contrib.auth.models import User
from s4sbackendapi.models import Users



class Samples(ViewSet):

    def create(self, request):

        user = User.objects.get(user=request.auth.user)
        sample = SamplesModel()

        try:
            sample.audio_url = request.data["audio_url"]
            sample.color = request.data["color"]
            sample.date_added = request.data["date_added"]
            sample.description = request.data["description"]
            sample.loudness = request.data["loudness"]
            sample.name = request.data["name"]
            sample.user = user
        except KeyError as ex:
            return Response({'Reason'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            sample.save()
            serializer = SampleSerializer(sample, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class SampleSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = Samples
        fields = ('audio_url', 'color', 'date_added', 'description', 'loudness', 'name', 'user')