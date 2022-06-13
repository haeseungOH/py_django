from django.shortcuts import render
from myvote.models import Question, Choice

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def dispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list':q_list}
    return render(request, 'display.html', context)


def detailFunc(request, question_id):
    pass

def voteFunc(request, question_id):
    pass

def resultFunc(request, question_id):
    pass

