from django.shortcuts import render

# Create your views here.
def home(request):
    restaurant_name = "Flavor Fiesta"
    return render(request "home.html",{"restaurant_name":restaurant_name})