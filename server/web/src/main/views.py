from django.views import generic
from django.shortcuts import render
from .lock_handler import lock
from .lock_handler import unlock
from .lock_handler import get_status
# from lock_handler import getStatus, lock, unlock
# Create your views here.


class Top(generic.TemplateView):
    template_name = 'top.html'


def locking(request):
    template_name = 'lock.html'

    status = lock()
    params = {
        'status': status,
    }

    return render(request, template_name, params)


def menu(request):
    template_name = 'menu.html'

    _status = get_status()

    params = {
        'status': _status,
    }

    return render(request, template_name, params)


def unlocking(request):
    template_name = 'unlock.html'

    status = unlock()
    params = {
        'status': status,
    }

    return render(request, template_name, params)


def _get_status(request):
    template_name = 'status.html'
    _status = get_status()
    params = {
        'status': _status,
    }

    return render(request, template_name, params)
