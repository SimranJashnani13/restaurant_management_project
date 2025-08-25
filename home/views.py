from django.shortcuts import render

# Create your views here.
def home(request):
    restaurant_name = "Flavor Fiesta"
    return render(request "home.html",{"restaurant_name":restaurant_name})

def about(request):
    restaurant_name = "Flavor Fiesta"
    description = (
        "Flavor Fiesta is a cozy restaurant serving freshly made dishes with love."
        "We combine traditional dishes with modern flavours to give you dining experience worth remembering. "
    )
    return render(request "about.html",
    {"restaurant_name":restaurant_name,
     "description":description})

def menu_items(request):
    items = [
        {"name" : "Margherita Pizza" , "price" : 250},
        {"name" : "Veggie Burger" , "price" : 150},
        {"name" : "French Fries" , "price" : 120},
        {"name" : "Pasta Alfredo" , "price" : 300},
        {"name" : "Cold Coffee" , "price" : 100},
    ]
    return render(request "menu.html",{"items" : items})

def contact(request):
    return render(request,"contact.html")

def homepage(request):
    phone_number = settings.RESTAURANT_PHONE
    return render(request "home.html", {"phone_number":phone_number})
