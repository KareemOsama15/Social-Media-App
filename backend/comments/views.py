from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer


class CommentCreate(APIView):

	def post(self,request):
		serializers = CommentSerializer(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data , status = status.HTTP_201_CREATED)
		return Response(serializers.errors , status = status.HTTP_400_BAD_REQUEST)

class CommentDelete(APIView):

	def destroy(self,request,pk):
		try:
			comment = Comments.objects.get(pk=pk)
		except Comment.DoesNotExists:
			raise Http404

		comment.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)

class CommentOfPost(APIView):

   def get(self,request,pk):
   	 comment = Comment.objects.filter(post=pk)
   	 serializers = CommentSerializer(comment,many=True)
   	 return Response(serializers.data)
