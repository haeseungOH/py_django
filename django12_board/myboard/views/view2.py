from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from myboard.models import BoardTab
from datetime import datetime

def replyFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
        context = {'data_one':data}
        return render(request, 'rep/reply.html', context)
    
    except Exception as e:
        print('댓글 대상자료 읽기 오류:', e)
        return render(request, 'error.html')
        
def replyOkFunc(request):
    if request.method == 'POST':
        try:
            repGnum = int(request.POST.get('gnum'))
            repOnum = int(request.POST.get('onum'))
            imsiRec = BoardTab.objects.get(id=request.POST.get('id'))
            # print('repGnum : ', repGnum)
            # print('repOnum : ', repOnum)
            # print(imsiRec)
            oldGnum = imsiRec.gnum
            oldOnum = imsiRec.onum
            
            if oldOnum >= repOnum and oldGnum == repGnum:
                oldOnum = oldOnum + 1   # onum 갱신
            
            # 댓글 저장
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'],
                bdate = datetime.now(),
                readcnt = 0,
                gnum = repGnum,
                onum = oldOnum,
                nested = int(request.POST.get('nested')) + 1,    
            ).save()    
            
            return redirect('/board/list')  # 댓글 저장 후 목록 보기
        except Exception as e:
            print('댓글 저장 오류', e)
            return render(request, 'error.html')
