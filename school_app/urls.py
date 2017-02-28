from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^detail/(?P<school_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^ask/$', views.save_enquiry, name='save_enquiry')
]
