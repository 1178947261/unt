from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField('标题', max_length=200)
    pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.question_text
    #用于判断问卷是否最近时间段内发布度的：
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    '''
    如果给定的字符串是模型的一种方法，那么如果您给这个方法一个布尔属性值为True，
    那么模型管理员或返回True或False Django的callable将显示一个漂亮的“on”或“off”图标。
    '''
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '是否是最近出版的?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #返回选择的字段
    def __str__(self):
        return self.choice_text