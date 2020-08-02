from django.shortcuts import render

def home_page(request):
    context = {
        "title":"Welcome to our brand new",
        "content":"Best E-Store to buy goods.",

    }
    return render(request, "home_page.html", context)
