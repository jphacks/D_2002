from django.views import generic
from django.shortcuts import render

from .lock_handler import MangeContract


class Top(generic.TemplateView):
    template_name = 'top.html'


contract_manager = MangeContract()


def locking(request):
    template_name = 'lock.html'

    status = contract_manager.lock()
    params = {
        'status': status,
    }

    return render(request, template_name, params)


def menu(request):
    template_name = 'menu.html'

    _status = contract_manager.get_status()

    params = {
        'status': _status,
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
    _status = contract_manager.get_status()
    params = {
        'status': _status,
    }

    return render(request, template_name, params)
