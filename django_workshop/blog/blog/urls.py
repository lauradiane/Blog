from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^blog/', include('posts.urls', namespace='blog')),	
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
