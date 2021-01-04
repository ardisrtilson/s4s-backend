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
import uuid
import base64
from django.core.files.base import ContentFile

class Samples(ViewSet):

    def create(self, request):

        user = s4sUser.objects.get(user=request.auth.user)
        sample = SamplesModel()
        sample.user = user
        try:
            sample.audio_url = request.data["audio_url"]
            sample.date_added = request.data["date_added"]
            sample.name = request.data["name"]
            format, imgstr = request.data['sample_image'].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["name"]}-{uuid.uuid4()}.{ext}')
            sample.sample_image = data
            sample.uploader = user
        except KeyError as ex:
            return Response({'Reason'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            sample.save()
            serializer = SampleSerializer(sample, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            sample = SamplesModel.objects.get(pk=pk)
            serializer = SampleListSerializer(sample, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        samples = SamplesModel.objects.all()

        serializer = SampleListSerializer(
            samples, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single comment
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            sample = SamplesModel.objects.get(pk=pk)
            sample.delete()
            #if succesful it will return a status code of 204
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        #if the object to be deleted doesn't exist status code will be 404
        except SamplesModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for a comments
        Returns:
            Response -- Empty body with 204 status code
        """
        user = s4sUser.objects.get(user=request.auth.user)

        sample = SamplesModel.objects.get(pk=pk)

        sample.audio_url = request.data["audio_url"]
        sample.date_added = request.data["date_added"]
        sample.name = request.data["name"]
        sample.sample_image = request.data["sample_image"]
        sample.uploader = user

        sample.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

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
        fields = ('audio_url', 'date_added', 'name', 'uploader', 'user', 'sample_image')

class SampleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamplesModel
        fields = ('audio_url', 'date_added', 'name', 'uploader', 'id', 'sample_image')