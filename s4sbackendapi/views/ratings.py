from s4sbackendapi.models.s4sUser import s4sUser
from django import utils
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from s4sbackendapi.models import SampleRatings as RatingsModel
from django.contrib.auth.models import User
from s4sbackendapi.models import Samples as SamplesModel

class SampleRatings(ViewSet):

    def create(self, request):

        user = s4sUser.objects.get(user=request.auth.user)
        rating = RatingsModel()
        rating.user = user
        try:
            rating.sample_id = request.data["sample"]
            rating.color = request.data["color"]
            rating.rating = request.data["rating"]
            rating.loudness = request.data["loudness"]
        except KeyError as ex:
            return Response({'Reason'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            rating.save()
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        ratings = RatingsModel.objects.all()

        serializer = RatingSerializer(
            ratings, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            ratings = RatingsModel.objects.all()
            serializer = RatingSerializer(ratings, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = RatingsModel
        fields = ('rating', 'color', 'user', 'sample', 'loudness')
        depth = 1