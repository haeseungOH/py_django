from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def dispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list':q_list}
    return render(request, 'display.html', context)


def detailFunc(request, question_id):
    # print(question_id)
    # return HttpResponse("question_id %s"%question_id)
    
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question 테이블은 없어요")      # 404에러를 내보냄(redirect)
    """
    # get_object_or_404(모델클래스, 검색조건) : 모델클래스에서 조건에 맞는 자료를 읽음
    # 그런데 자료(모델클래스)가 없는 경우 Http404 exception을 발생시키는 함수  
    question = get_object_or_404(Question, pk=question_id)
    
    # print(question.question_text)
    # print(question.pub_date)
    print(question)
    # fk로 연결된 Choice 테이블 자료 보기
    # print('question.choice_set.all() : ',question.choice_set.all())
    for ch in question.choice_set.all():
        print(ch.choice_text)
        
    return render(request, 'detail.html', {'question':question})

     
        
def voteFunc(request, question_id):
    # print(request.POST.get('choice'))
    # return HttpResponse("선택한 항목은 %s"%question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel_choice = question.choice_set.get(pk=request.POST.get('choice'))
        # print('sel_choice : ', sel_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'error_msg':'1개의 항목을 선택하세요'})
    
    # reverse : url 패턴으로 부터 url string 얻기
    # print(reverse('results', args=(question_id,)))  # /gogo/1/results/
    
    # 선택된 항목을 DB에 저장
    sel_choice.votes += 1
    sel_choice.save() 
    return HttpResponseRedirect(reverse('results', args=(question_id,)))
    
    
def resultFunc(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question':question})

