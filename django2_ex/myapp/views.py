from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")

def sendFunc(request):
    msg = request.GET['msg']
    gen = request.GET['gen']
    return render(request, 'show.html', {'msg':msg, 'gen':gen})
    