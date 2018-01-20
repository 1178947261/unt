from django.shortcuts import *
from .models import *
# Create your views here.


def index(request):
    '''

    :param request:
    :return:
    latest_question_list = 数据库内数据
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request,"polls/index.html",context)


def detail(request, question_id):
    '''
    :param request:
    :param question_id:
    :return:渲染视图
    :get_object_or_404 取出数据错误就像用户~展示出~404 页面
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html', {'question': question})


def vote(request, question_id):
    '''


    :param request:
    :param question_id:
    :param question_id:
    :param selected_choice: model数据对象
    :return:
    '''

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:

        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))