from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.post_list, name='list'),
	url((r'^read/(?P<slug>[-\w]+)/$'), views.post_detail, name='detail'),
)
