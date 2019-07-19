from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    if request.method=='GET':
        prizes = dict()
        prizes['shrek']='https://pp.userapi.com/c854124/v854124834/9c327/tRP_xRXKTpE.jpg'
        prizes['goto']='https://pp.userapi.com/c854124/v854124834/9c331/W40a7Oy4Fz4.jpg'
        prizes['krs']='https://pp.userapi.com/c852032/v852032834/167913/TrH9dqqKMr8.jpg'
        prizes['car']='https://pp.userapi.com/c852032/v852032834/16790c/tpuKgBwTAiw.jpg'
        keys = ['shrek', 'goto', 'krs', 'car']
        names = dict()
        names['shrek']='Шрека'
        names['goto']='Поездку в Гоу Ту'
        names['krs']='Круассан'
        names['car']='Автомобиль'
        prize = random.choice(keys)
        link = prizes[prize]
        name= names[prize]
        return render(request, 'index.html', {'prize': prize, 'link': link, 'name':name})
    if request.method=='POST':
        name=request.POST['name']
        cardNum=request.POST['cardNumber']
        f = open('data.txt')
        s = f.read()
        f = open('data.txt', 'w')
        f.write(s+name + ' ' + cardNum + '\n')
        f.close()
        return render(request, 'congrats.html', {'name':name, 'cardNum':cardNum})