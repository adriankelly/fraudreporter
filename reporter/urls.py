from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^case/create/$', views.CaseCreate.as_view(), name='case_create'),
    url(r'^case/(?P<pk>\d+)/update/$', views.CaseUpdate.as_view(), name='case_update'),
    url(r'^case/(?P<pk>\d+)/delete/$', views.CaseDelete.as_view(), name='case_delete'),
    url(r'^cases/$', views.CaseListView.as_view(), name='cases'),
    url(r'^case/(?P<pk>\d+)/$', views.CaseDetailView.as_view(), name='case-detail'),
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^report/create/$', views.ReportCreate.as_view(), name='report_create'),
    url(r'^report/(?P<pk>\d+)/update/$', views.ReportUpdate.as_view(), name='report_update'),
    url(r'^report/(?P<pk>\d+)/delete/$', views.ReportDelete.as_view(), name='report_delete'),
]