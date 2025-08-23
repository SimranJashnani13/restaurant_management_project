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