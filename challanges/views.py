import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challangess = {
    "january": "Do not eat meat!",
    "february": "go for a walk for 20 mins!",
    "march": "study django for 20 mins atleast!",
    "april": "Do not eat meat!",
    "may": "go for a walk for 20 mins!",
    "june": "study django for 20 mins atleast!",
    "july": "Do not eat meat!",
    "august": "go for a walk for 20 mins!",
    "september": "study django for 20 mins atleast!",
    "october": "Do not eat meat!",
    "november": "go for a walk for 20 mins!",
    "december": "study django for 20 mins atleast!"
}

def index(request):
    list_items =""
    months = list(monthly_challangess.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challange", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challanges_by_number(request, month):

    months = list(monthly_challangess.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challange",args=[redirect_month]) # challenge/january 
    return HttpResponseRedirect(redirect_path)


def monthly_challanges(request, month):
    try:
        challange_text = monthly_challangess[month]
        return render(request,"challanges/challange.html",{
            "text":challange_text,
            "month_name":month
        })
        #response_data=render_to_string("challanges/challange.html")
        #return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>this month does not match!</h1>")
