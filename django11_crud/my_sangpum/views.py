from django.shortcuts import render, redirect
from my_sangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def MainFunc(request):
    return render(request,'main.html')

def ListFunc(request):
    """
    sql = "select * from sangdata"
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fatchall()
    ...
    """
    # 페이지 나누기 안함
    # datas = Sangdata.objects.all()
    # return render(request, 'list.html', {'sangpums':datas})
    
    # 페이지 나누기
    datas = Sangdata.objects.all().order_by('-code')
    paginator = Paginator(datas, 5)     # 페이지 당 5 행씩 출력
    try:
        page = request.GET.get('page')
    except:
        page = 1
        
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
        
    # 개별 페이지 번호 표시를 원할 경우
    allpage = range(paginator.num_pages + 1)
    print('allpage: ',allpage)  # range(0,4)
        
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage})

def InsertFunc(request):
    return render(request, 'insert.html')   # forward 방식

def InsertOkFunc(request):
    if request.method == 'POST':
        # code = request.POST.get("code")
        # print(code)
        
        # 신상 code 중복 확인 후 추가 작업
        try:
            Sangdata.objects.get(code=request.POST.get("code"))
            return render(request, 'insert.html', {'msg':'이미 등록된 code입니다.'})
        except:
            Sangdata(
                code = request.POST.get("code"),
                sang = request.POST.get("sang"),
                su = request.POST.get("su"),
                dan = request.POST.get("dan")
            ).save()
            return HttpResponseRedirect("/sangpum/list") # redirect 방식
    
def UpdateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html', {'sang_one':data})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code'))
        upRec.code = request.POST.get('code')
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        upRec.save()
    
    return redirect("/sangpum/list") # redirect 방식

def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    return redirect("/sangpum/list")    # 삭제 후 상품 보기


