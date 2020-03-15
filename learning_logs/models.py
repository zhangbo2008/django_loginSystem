from django.db import models

# Create your models here.


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):  #  继承了Django基类Model 
    """学到的有关某个主题的具体指示"""

    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)  # 外键。每个主题创建时，都给它分配了一个键(或ID).  
    text = models.TextField()    # 不需要长度限制
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # 用于管理模型的额外信息，在需要时使用Entries来表示多个条目。若没有，将使用Entrys来表示多个条目。
        verbose_name_plural = 'entries'

    def __str__(self):    # 只呈现text前50个字符。
        """返回模型的字符串表示"""
        return self.text[:50] + "..."