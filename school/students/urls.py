# connect view ---> url
from django.urls import path

from .views import hello, hi, stdlist, second, newLsit

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hi', hi),
    path('list', stdlist),
    path('second',second),
    path('newList',newLsit)

]

