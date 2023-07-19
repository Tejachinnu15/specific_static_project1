from django.shortcuts import render

# Create your views here.
def bike(request):
    return render(request,'bike.html')
def about(request):
    return render(request,'about.html')
def prices(request):
    return render(request,'prices.html')
def model(request):
    return render(request,'model.html')