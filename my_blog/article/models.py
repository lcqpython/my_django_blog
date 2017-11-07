from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  # 文章标题
    category = models.CharField(max_length=50, blank=True)  # 文章分类
    date_time = models.DateTimeField(default=timezone.now)  # 文章创建时间
    content = models.TextField(blank=True, null=True)  # 文章内容

    # 如果没有这个方法，现实的是一个对象，相反，显示具体标题
    def __str__(self):
        return self.title

    class Meta:  # 倒排序
        ordering = ('-date_time',)