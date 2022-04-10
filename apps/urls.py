from django.urls import path
from .views import *

# from .views import index,SearchResultsView,category_detail
urlpatterns = [
    path('', index, name='home'),
    path('noldon', second, name='biznessnoldon'),
    path('akadem', third, name='aka'),
    path('log', log, name='login'),
    path('classes', allcourse, name='clas'),
    path('classes2', allcourse2, name='class'),
    path('syr', surtrening, name='syr'),
    path('zhanyzhashoo', janyjashoo, name='jany'),
    path('akchasarptoo', akcha, name='akcha'),
    path('express', express, name='express'),
    path('orator', orator, name='orator'),
    path('biznesstrenerzhardamaluu', jardam, name='jardam'),
    path('SMM', smm, name='smm'),
    path('russian', rus, name='rus'),
    path('login', login, name='login'),
    path('syrfull/', syrfull, name='syrfull')
]
