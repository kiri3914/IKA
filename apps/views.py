# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.core.paginator import Paginator
# from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import ListView,DetailView,CreateView
# from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.models import User
from .models import *


def index(request):
    return render(request, 'index.html')


def second(request):
    return render(request, 'biznesnoldon.html')


def third(request):
    return render(request, 'ishkerdikakademiya.html')


def log(request):
    return render(request, '4.html')

def allcourse(request):
    return render(request, 'classes.html')


def allcourse2(request):
    return render(request, 'classes2.html')


def surtrening(request):
    return render(request, 'syr.html')


def janyjashoo(request):
    return render(request, 'janyjashoo.html')


def akcha(request):
    return render(request, 'akchasarptoo.html')


def express(request):
    return render(request, 'expressbizness.html')


def orator(request):
    return render(request, 'oratorbloger.html')


def jardam(request):
    return render(request, 'biznesstrenerjardam.html')


def smm(request):
    return render(request, 'smmkurs.html')


def rus(request):
    return render(request, 'rus.html')


def login(request):
    return render(request, 'kiruu.html')


def create_view(request):
    pass
    # return render(request, "syrfull.html", context)


def syrfull(request):
    context = {}
    context['syrfull'] = Syrfull.objects.all()
    return render(request, 'syr-full.html', context)
#
# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'base.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Авторизация')
#         return dict(list(context.items()) + list(c_def.items()))
