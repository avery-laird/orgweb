from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^profile/(?P<user_id>\w{0,50})/$', views.profile, name="profile"),
    url(r'^edit/(?P<file_name>\w{0,50})/$', views.edit, name="org_edit"),
    url(r'^create/$', views.create, name="org_create"),
    url(r'^view/(?P<file_name>)/$', views.view, name="org_view"),
    url(r'^delete/([0-9]\w+)/$', views.delete, name="org_delete"),
]