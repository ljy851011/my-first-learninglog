"""定义learning_logs的url模式"""
from django.conf.urls import url
from . import views
urlpatterns = [
    #主页
    url(r'^$',views.index,name='index'),
    #显示所有主题
    url(r'^topics/$',views.topics,name='topics'),
    #特定主题的详细信息
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #用于添加新主题的网页
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
]
