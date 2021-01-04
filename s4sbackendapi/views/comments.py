from s4sbackendapi.models.s4sUser import s4sUser
from django import utils
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from s4sbackendapi.models import Comments as CommentsModel
from django.contrib.auth.models import User

class Comments(ViewSet):

    def create(self, request):

        user = s4sUser.objects.get(user=request.auth.user)
        comment = CommentsModel()
        comment.user = user
        try:
            comment.user = user
            comment.sample_id = request.data["sample"]
            comment.content = request.data["content"]
            comment.date_added = request.data["date_added"]
        except KeyError as ex:
            return Response({'Reason'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            comment.save()
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            comment = CommentsModel.objects.get(pk=pk)
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        comments = CommentsModel.objects.all()

        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single comment
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            comment = CommentsModel.objects.get(pk=pk)
            comment.delete()
            #if succesful it will return a status code of 204
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        #if the object to be deleted doesn't exist status code will be 404
        except CommentsModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for a comments
        Returns:
            Response -- Empty body with 204 status code
        """
        user = s4sUser.objects.get(user=request.auth.user)

        comment = CommentsModel.objects.get(pk=pk)

        comment.sample = request.data["sample"]
        comment.content = request.data["content"]
        comment.date_added = request.data["date_added"]

        comment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class MainUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class s4sUserSerializer(serializers.ModelSerializer):

    user = MainUserSerializer(many=False)

    class Meta:
        model = s4sUser
        fields = ('id', 'user', 'profile_image',)
        depth = 1

class CommentSerializer(serializers.ModelSerializer):

    user = s4sUserSerializer(many=False)

    class Meta:
        model = CommentsModel
        fields = ('id', 'user', 'sample', 'content', 'date_added',)