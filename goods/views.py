from django.shortcuts import render, get_object_or_404
from .models import Good, Contacts

def goods_list(request):
    contacts = Contacts.objects.all()
    goods = Good.objects.all()
    return render(request, 'goods/goods_list.html', {'goods': goods, 'contacts': contacts})

def index(request):
    contacts = Contacts.objects.all()
    goods = Good.objects.all()
    return render(request, 'goods/index.html', {'goods': goods, 'contacts': contacts})

def good(request, pk):
    #post = Post.objects.get(pk=pk)
    contacts = Contacts.objects.all()
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'goods/good.html', {'good': good, 'contacts': contacts})

def pay_delivery(request):
    contacts = Contacts.objects.all()
    return render(request, 'goods/pay_delivery.html', {'contacts': contacts})

def guarantee(request):
    contacts = Contacts.objects.all()
    return render(request, 'goods/guarantee.html', {'contacts': contacts})

def about(request):
    contacts = Contacts.objects.all()
    return render(request, 'goods/about.html', {'contacts': contacts})

def contacts(request):
    contacts = Contacts.objects.all()
    return render(request, 'goods/contacts.html', {'contacts': contacts})

def business(request):
    contacts = Contacts.objects.all()
    return render(request, 'goods/business.html', {'contacts': contacts})

def login(request):
    return render(request, 'goods/login.html')

def advantage(request):
    contacts = Contacts.objects.all()
    return render(request, 'goods/advantage.html', {'contacts': contacts})
