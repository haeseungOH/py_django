from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def indexFunc(request):                            # request를 꼭 작성하여야 한다. 서버 첫 화면 변경 함수
    #return HttpResponse('요청 처리 결과')            # django.http.response
    
    msg = '장고 만세'
    ss = "<html><body>장고 프로젝트 구현 %s</body></html>" %msg
    return HttpResponse(ss)                        # django.http.response

def showFunc(request):
    msg = '파이썬 어쩌구 저쩌구'
    
    return render(request,'show.html', {'mymsg':msg})             # forward 방식
