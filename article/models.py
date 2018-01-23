from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100) #博客题目
    category = models.CharField(max_length=50, blank=True)#博客标签
    date_time = models.DateTimeField(auto_now_add=True) #博客日期
    content = models.TextField(blank = True, null = True) #博客文章正文

    def get_absolute_url(self):
        path = reversed('detail', kwargs = {'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    #按时间下降排序
    class Meta:
        ordering = ['-date_time']