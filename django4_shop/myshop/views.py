from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def page1Func(request):
    return render(request, 'page1.html')

def page2Func(request):
    return render(request, 'page2.html')

def cartFunc(request):
    name = request.POST['name']
    price = request.POST['price']
    print(name, price)
    product = {'name':name, 'price':price}
    
    productList = []
    if "shop" in request.session:
        productList = request.session['shop']
        productList.append(product)
        request.session['shop'] = productList
        
    else:
        productList.append(product)
        request.session['shop'] = productList       # 상품을 담는 productList클래스 생성 
        
    print(productList)
    context = {}    # html에 보낼 용도        html에 보낼때는 key value로 보내야 한다.
    context['products'] = request.session['shop']
    return render(request, 'cart.html',context)
    
def buyFunc(request):
    if "shop" in request.session:
        productList = request.session['shop']
        print(productList)
        
        total = 0
        for pro in productList:
            total += int(pro['price'])
        print(total)
        request.session.clear()     #session 안에 모든 키 삭제
        
    return render(request, 'buy.html',{'total':total})       