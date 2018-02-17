from django.shortcuts import render, get_object_or_404
from .models import Good, Contacts

def goods_list(request):
    goods = Good.objects.all()
    return render(request, 'goods/goods_list.html', {'goods': goods})

def index(request):
    goods = Good.objects.all()
    return render(request, 'goods/index.html', {'goods': goods})

def good(request, pk):
    #post = Post.objects.get(pk=pk)
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'goods/good.html', {'good': good})

def pay_delivery(request):
    return render(request, 'goods/pay_delivery.html')

def guarantee(request):
    return render(request, 'goods/guarantee.html')

def about(request):
    return render(request, 'goods/about.html')

def contacts(request):
    contact = Contacts.objects.all()
    return render(request, 'goods/contacts.html', {'contacts': contacts})