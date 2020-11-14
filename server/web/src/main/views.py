from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

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

        params = {
            'status': status,
            'price': price,
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
        form.instance.abi = "ここにabi(string)を代入"
        form.instance.tx_hash = "ここにtx_hash(string)を代入"
        return super(ProductRegister, self).form_valid(form)


class ProductRegisterDone(generic.TemplateView):
    template_name = 'product_register_done.html'
