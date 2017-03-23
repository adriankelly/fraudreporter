from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cases/$', views.CaseListView.as_view(), name='cases'),
    url(r'^case/(?P<pk>\d+)/$', views.CaseDetailView.as_view(), name='case-detail'),

]