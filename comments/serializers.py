from rest_framework import serializers, viewsets
from models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'author', 'text')
