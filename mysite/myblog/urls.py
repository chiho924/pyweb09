from django.conf.urls import url, include
from django.contrib.auth.models import User

from myblog.views import stub_view
from myblog.views import list_view
from myblog.views import detail_view

from myblog.views import PostCreate, PostUpdate, PostDelete


urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name='blog_detail'),
    url(r'post/add/$', PostCreate.as_view(), name='blog_detail'),
    url(r'post/(?P<pk>[0-9]+)/$', PostUpdate.as_view(), name='post-update'),
    url(r'post/(?P<pk>[0-9]+)/delete/$', PostDelete.as_view(), name='post-delete'),

]
