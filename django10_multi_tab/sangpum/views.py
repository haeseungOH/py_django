from django.shortcuts import render
from sangpum.models import Maker, Product
from django.db.models.aggregates import Sum, Avg, StdDev, Count

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def List1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html',{'makers':makers})

def List2(request):
    products = Product.objects.all()
    pcount = len(products)

    print(Product.objects.all().count())   # 건수 출력
    
    for r in products.values_list():  # tuple type으로 모두 출력
        print(r)
    
    print(products.aggregate(Count('price')))  # {'price__count': 4}
    print(products.aggregate(Sum('price')))    # {'price__sum': 86000}
    print(products.aggregate(Sum('price'))['price__sum'])  # 86000
    print(products.aggregate(Avg('price')))
    print(products.aggregate(StdDev('price')))
    print()
    aa = products.filter(pname='치킨버거')   # 얘네들만 제외
    for r in aa.values_list():
        print(r)       # (2, '치킨버거', 9000, 2)
    
    print('---')
    bb = products.exclude(pname='치킨버거')  # 얘만 제외한 나머지들
    for r in bb.values_list():
        print(r)

    return render(request, 'list2.html',{'products':products, 'pcount':pcount})

def List3(request):
    mid = request.GET.get('id')
    products = Product.objects.filter(maker_name=mid)
    pcount = len(products)
    return render(request, 'list2.html',{'products':products, 'pcount':pcount})