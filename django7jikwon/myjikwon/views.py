from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from myjikwon.models import Jikwon

plt.rc('font', family='malgun gothic')

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def showFunc(request):
    jikwons = Jikwon.objects.all().values()     # list type 안에 dict로 담기 <QuerySet [{'jikwon_no': 1, 'jikwon_name': '홍길동'....
    #print(jikwons)
    df = pd.DataFrame.from_records(data = jikwons)
    df.columns = ['사번','직원명','부서','직급','연봉','입사','성별','평점']
    print(df.head(2))
    
    # 부서별 연봉합/평균
    buser_group = df['연봉'].groupby(df['부서'])
    buser_group_detail = {'sum':buser_group.sum(), 'avg':buser_group.mean()}
    print(buser_group_detail, type(buser_group_detail))
    
    # 부서별 연봉합/평균 -> DataFrame
    print('--df2------------------')
    df2 = pd.DataFrame(buser_group_detail)
    print(df2)
    
    #시각화 이미지로 저장
    bu_result = buser_group.agg(['sum','mean'])
    print(bu_result)
    
    bu_result.plot(kind='barh')
    plt.title('부서별 연봉합/평균')
    plt.xlabel('연봉')
    fig = plt.gcf()
    fig.savefig('django7jikwon/myjikwon/static/images/buser.png')   # static folder에 저장
    
       
    return render(request, 'list.html', 
                  {'datas':df.to_html(index=False), 'buser_group':buser_group_detail,
                                         'buser_group2':df2.to_html()})

    
    