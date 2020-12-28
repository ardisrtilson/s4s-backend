from django import utils
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from s4sbackendapi.models import UserSkipped as SkippedModel
from s4sbackendapi.models import s4sUser
from django.contrib.auth.models import User

class UserSkipped(ViewSet):

    def create(self, request):

        user = s4sUser.objects.get(user=request.auth.user)
        user_id = user.id
        skipped = SkippedModel()
        try:
            skipped.sample_id = request.data["sample"]
            skipped.user_id = user_id
        except KeyError as ex:
            return Response({'Reason'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            skipped.save()
            serializer = SkippedSerializer(skipped, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            skipped = SkippedModel.objects.get(pk=pk)
            serializer = SkippedSerializer(skipped, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        skipped = SkippedModel.objects.all()

        serializer = SkippedSerializer(
            skipped, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single comment
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            skipped= SkippedModel.objects.get(pk=pk)
            skipped.delete()
            #if succesful it will return a status code of 204
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        #if the object to be deleted doesn't exist status code will be 404
        except SkippedModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SkippedSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = SkippedModel
        fields = ('sample_id', 'user_id', 'id')