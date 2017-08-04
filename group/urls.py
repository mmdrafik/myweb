from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^group/new/$', views.group_new, name="group_new"),
    url(r'^group/(?P<group_id>\d+)/$', views.group_detail, name='group_detail'),
    url(r'^group/(?P<group_id>\d+)/edit/$', views.group_edit, name='group_edit'),
    url(r'^member/new/$',views.member_new, name="member_new"),
    url(r'^member/(?P<member_id>\d+)/$', views.member_detail, name="member_detail"),
    url(r'^member/(?P<member_id>\d+)/edit/$', views.member_edit, name='member_edit'),
]
