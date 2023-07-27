from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def contact(request):
    html = '<html><body>欢迎咨询</body></html>'
    return HttpResponse(html)

def recruit(request):
    html = '<html><body>加入我们</body></html>'
    return HttpResponse(html)