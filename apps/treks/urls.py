from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /treks/
    url(r'^$', views.index, name='index'),
    # ex: /treks/5/
    url(r'^(?P<trek_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /treks/5/route/
    url(r'^(?P<trek_id>[0-9]+)/route/$', views.route, name='route'),
]