from django.shortcuts import render

# Create your views here.
def company(request):
    return render(request,'company.html')

def industry(request):
    return render(request,'industry.html')

def notice(request):
    return render(request,'notice.html')