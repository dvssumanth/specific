from django.urls import path
from app2.views import *
app_name='apl'
urlpatterns=[
    path('dvs/',dvs,name='dvs'),
    path('ani/',ani,name='ani'),
    path('satya/',satya,name='satya'),
]