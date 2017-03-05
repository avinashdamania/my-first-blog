from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list')
	url(r'^$', views.post_list, name='create')
	url(r'^$', views.post_list, name='signin')
	url(r'^$', views.post_list, name='signup')
	url(r'^$', views.post_list, name='support')
	url(r'^$', views.post_list, name='upload')
]