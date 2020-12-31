from s4sbackendapi.models.s4sUser import s4sUser
from django import utils
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from s4sbackendapi.models import Samples as SamplesModel
from s4sbackendapi.models import UserFavorites as FavoritesModel
from django.contrib.auth.models import User
from random import choice

class RandomSample(ViewSet):

    def list(self, request):
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        # notUser = SamplesModel.objects.exclude(uploader=request.auth.user.id)
        # pks = notUser.values_list('pk', flat=True)
        # random_pk = choice(pks)
        # random_obj = SamplesModel.objects.get(pk=random_pk)

        notUser = SamplesModel.objects.exclude(uploader=request.auth.user.id)
        shuffledSamples = notUser.order_by('?')

        serializer = SampleListSerializer(
            shuffledSamples, many=True, context={'request': request})
        return Response(serializer.data)

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
        fields = ('audio_url', 'color', 'date_added', 'loudness', 'name', 'uploader', 'user', 'sample_image')

class SampleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamplesModel
        fields = ('audio_url', 'color', 'date_added', 'loudness', 'name', 'uploader', 'id', 'sample_image')