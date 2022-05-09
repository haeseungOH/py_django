from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import json
from jikwonapp.models import Jikwon

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

@csrf_exempt
def PredictFunc(request):
    year = request.POST['year']
    new_val = pd.DataFrame({'year':[year]})
    # print(new_val)
    
    # 모델 생성
    datas = Jikwon.objects.values('jikwon_ibsail','jikwon_pay','jikwon_jik').all()
    jikwon = pd.DataFrame.from_records(datas)
    #print(jikwon)
    
    # 근무년수 구하기
    for i in range(len(jikwon['jikwon_ibsail'])):
        jikwon['jikwon_ibsail'][i] = int((datetime.now().date() - jikwon['jikwon_ibsail'][i]).days / 365)
    
    jikwon.columns = ['근무년수', '연봉', '직급']
    # print(jikwon)
    
    train_set, test_set = train_test_split(jikwon, test_size = 0.2)
    print(train_set.shape, test_set.shape)  # (24, 3) (6, 3)
    
    # model
    model_lr = LinearRegression().fit(X = train_set.iloc[:,[0]], y = train_set.iloc[:,[1]])
    
    test_pred = model_lr.predict(test_set.iloc[:,[0]])
    test_real = test_set.iloc[:, 1]
    # print('예측값 : ', test_pred)
    # print('실제값 : ', test_real)
    
    lin_mse = mean_squared_error(test_real, test_pred)
    lin_rmse = np.sqrt(lin_mse)
    print('RMSE : ', lin_rmse)
    r2 = r2_score(test_real, test_pred)
    print('r2_score : ', r2)  # 0.831463
    
    # 새로운 값 예측
    new_pred = round(model_lr.predict(new_val)[0][0], 2)
    print(new_pred)
    
    # 직급별 연봉 평균
    pay_jik = jikwon.groupby('직급').mean().round(1)
    pay_jik2 = pay_jik.to_html()
    
    # return JsonResponse({'new_pred':new_pred, 'pay_jik':pay_jik2, 'r2':r2})
    
    context = {'new_pred':new_pred, 'pay_jik':pay_jik2, 'r2':r2}
    return HttpResponse(json.dumps(context), content_type='application/json')

