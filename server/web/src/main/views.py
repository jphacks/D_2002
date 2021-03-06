from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

from rest_framework import viewsets, filters
from .serializer import ProductSerializer

from .manager import ContractManager
from .forms import (
    ProductRegistrationForm
)
from .models import (
    Product
)

contract_manager = ContractManager()


class Top(generic.TemplateView):
    template_name = 'top.html'


def locking(request):
    template_name = 'lock.html'

    status = contract_manager.lock()
    params = {
        'status': status,
    }

    return render(request, template_name, params)


def menu(request):
    template_name = 'menu.html'

    status = contract_manager.get_status()
    
    if status == 'Locked':
        price = contract_manager.get_price()
        product = Product.objects.last()

    
        params = {
            'status': status,
            'price': product.price,
            'name' : product.name,
            'amount' : product.amount,
            'intro': product.intro,
            'image' : product.image,
            'tx_hash': product.tx_hash,
        }
    else:
        params = {
            'status': status,
        }

    return render(request, template_name, params)


def unlocking(request):
    template_name = 'unlock.html'

    status = contract_manager.unlock()
    params = {
        'status': status,
    }

    return render(request, template_name, params)


def _get_status(request):
    template_name = 'status.html'
    status = contract_manager.get_status()
    params = {
        'status': status,
    }

    return render(request, template_name, params)


class History(generic.TemplateView):
    template_name = 'history.html'


# class ProductRegister(generic.TemplateView):
#     template_name = 'product_register.html'


class ProductRegister(generic.CreateView):
    model = Product
    form_class = ProductRegistrationForm
    template_name = 'product_register.html'
    success_url = reverse_lazy('main:product_register_done')

    def form_valid(self, form):
        tx_hash = contract_manager.deploy_contract(int(form.cleaned_data['price']))
        form.instance.tx_hash = tx_hash
        return super(ProductRegister, self).form_valid(form)


class ProductRegisterDone(generic. DetailView):
    model = Product
    

    def get_context_data(self):
        product = Product.objects.last()
        context = super().get_context_data(self)
        context['name'] = product.name
        context['amount'] = product.amount
        context['price'] = product.price
        context['intro'] = product.intro
        context['image'] = product.image
        context['tx_hash'] = product.tx_hash
        return context


def product_register_done(request):
    template_name = 'product_register_done.html'
    product = Product.objects.last()
    
    params = {
        'name' : product.name,
        'amount' : product.amount,
        'price': product.price,
        'intro': product.intro,
        'image' : product.image,
        'tx_hash': product.tx_hash,
    }

    return render(request, template_name, params)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() # 最新のデータを取得
    serializer_class = ProductSerializer
