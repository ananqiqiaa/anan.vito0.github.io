from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('company/',views.company,name='company'),
    path('industry/',views.industry,name='industry'),
    path('notice/',views.notice,name='notice'),
]