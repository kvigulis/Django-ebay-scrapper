from django.conf.urls import url
from . import views

app_name = 'miner'

urlpatterns = [
    # /miner/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /miner/<pk>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /miner/filter/add/
    url(r'filter/add/$', views.FilterCreate.as_view(), name='filter-add'),
    # /miner/filter/2/
    url(r'filter/(?P<pk>[0-9]+)/$', views.FilterUpdate.as_view(), name='filter-update'),
    # /miner/filter/2/delete/
    url(r'filter/(?P<pk>[0-9]+)/delete/$', views.FilterDelete.as_view(), name='filter-delete'),
    # /miner/result/2/delete/
    url(r'filter/(?P<pk>[0-9]+)/delete/$', views.ResultDelete.as_view(), name='result-delete'),
    # /miner/2/favorite_filter/
    url(r'^(?P<album_id>[0-9]+)/favorite_filter/$', views.favorite_filter, name='favorite_filter'),
    # /miner/run/
    url(r'run/$', views.run_testScript, name='run'),
]
