from django.conf.urls import patterns,url
from  blog import views
urlpatterns=patterns(
'blog.views',
url(r'^$',views.index, name='index'),
url(r'^add_post/',views.add_post, name='add_post'),
#url(r'^(?P<post_id>\d+)/$',views.post,name='post'),
#url(r'^(?P<post_url>\w+)/$',views.post, name='post'),
url(r'^(?P<slug>[]\w|\-]+)/$',views.post, name='post'),
)
