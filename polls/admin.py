from django.contrib import admin
from .models import *




class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''
      字段的先后排序
      Choice对象将在Question管理页面进行编辑，默认情况，请提供3个Choice对象的编辑区域。
      :param  list_display:显示的字段
      :param list_filter 过滤字段
      :param search_fields 搜索~字段
      :param fieldsets 字段标题
      :param was_published_recently 状态
      '''
    fieldsets = [
        ('标题',               {'fields': ['question_text']}),
        ('时间', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    date_hierarchy = 'pub_date'

# admin.site.register(Question, QuestionAdmin)