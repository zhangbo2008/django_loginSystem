from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def index(request):
    """学习笔记的主页"""
    return render(request, 'index.html')
from .models import Topic
@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据:创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics')) # 重新调回topic网页.  reverse('learning_logs:topics') 返回这个名称的url.
    context = {'form': form}
    return render(request, 'new_topic.html', context)


from .forms import TopicForm,EntryForm
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)