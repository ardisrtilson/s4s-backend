from django import utils
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from s4sbackendapi.models import s4sUser as s4sUserModel

class Profiles(ViewSet):

    def list(self, request):
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        users = s4sUserModel.objects.all()

        serializer = s4sUserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)

class MainUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class s4sUserSerializer(serializers.ModelSerializer):

    user = MainUserSerializer(many=False)

    class Meta:
        model = s4sUserModel
        fields = ('id', 'sex', 'user')
        depth = 1