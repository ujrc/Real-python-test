from django.conf.urls import patterns,url
from hello_world import views

urlpatterns=patterns(
'hello_world.views',
url(r'^$',views.index, name='index'),
url(r'^about/',views.about,name='about'),
url(r'^contact/', views.contact, name='contact'),
url(r'^better/$', views.better, name='better'),
)
