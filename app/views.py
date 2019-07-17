from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request, 'index.html')
    if request.method=='POST':
        name=request.POST['name']
        cardNum=request.POST['cardNumber']
        f = open('data.txt')
        s = f.read()
        f = open('data.txt', 'w')
        f.write(s+name + ' ' + cardNum + '\n')
        f.close()
        return render(request, 'congrats.html', {'name':name, 'cardNum':cardNum})