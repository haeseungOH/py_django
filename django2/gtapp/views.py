from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, "index.html")

class CallView(TemplateView):
    template_name = "callget.html"

""" 
def insertFunc(request):
    return render(request, 'insert.html')

def insertokFunc(request):                  # client 에게 받을때는 request / 보낼때는 response
    #irum = request.GET.get('name')         # 2개는 같은 get 방식   
    irum = request.GET['name']                  
    print(irum)
    
    return render(request, 'list.html', {'irum':irum})      # irum을 넘길때 {'irum':irum}
"""    

def insertFunc(request):                          # insert get방식과 post 방식을 한번에 쓰기
    if request.method == 'GET':
        print('GET 요청 처리')
        return render(request, 'insert.html')     # forward 방식 ex)<jsp:
        
    elif request.method == 'POST':
        print('POST 요청 처리')
        irum = request.POST.get('name')
        return render(request, 'list.html', {'irum':irum})
    
    else:
        print('요청 에러') 
    