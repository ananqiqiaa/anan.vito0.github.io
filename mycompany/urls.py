"""mycompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.views import home
from science.views import science
from django.conf import settings
from django.conf.urls.static import static
from products.views import products,productDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contact/',include('contact.urls')),
    path('introduce/',include('introduce.urls')),
    path('news/',include('news.urls')),
    path('science/',science,name='science'),
    path('products/<str:productName>/', products, name="products"),
    path('pd/<int:id>/', productDetail, name="pd"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


