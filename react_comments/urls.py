
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, viewsets
from comments.serializers import CommentSerializer
from comments.models import Comment

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

router = routers.DefaultRouter()
router.register(r'api-comments', CommentViewSet)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^comments/', include('comments.urls', namespace='comments')),
]
