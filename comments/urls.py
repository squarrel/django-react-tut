from django.conf.urls import url, include
from comments import views

urlpatterns = [
	url('^$', views.index)
]
