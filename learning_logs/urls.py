"""定义learning_logs的URL模式"""

from django.conf.urls import url   # 函数url用于创建URL映射到视图

from . import views    # 当前的urls.py模块所在的文件夹中导入视图

app_name='learning_logs'  # 防止出现错误：Specifying a namespace in include() without providing an app_name

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    # url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
# (?P<topic_id>\d+)  把一个数字绑定到变量topic_id中.
]