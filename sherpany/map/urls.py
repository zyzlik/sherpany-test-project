from django.conf.urls import url

from .views import MapView, SaveLocationView, ResetTablesView

urlpatterns = [
    url(r'^$', MapView.as_view(), name='index'),
    url(r'^save/$', SaveLocationView.as_view(), name='save_location'),
    url(r'^reset/$', ResetTablesView.as_view(), name='reset'),
]
