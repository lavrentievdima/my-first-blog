from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^goods/$', views.goods_list, name='goods_list'),
    url(r'^good/(?P<pk>\d+)/$', views.good, name='good'),

    url(r'^pay_delivery/$', views.pay_delivery, name='pay_delivery'),
    url(r'^guarantee/$', views.guarantee, name='guarantee'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contacts, name='contacts'),

]