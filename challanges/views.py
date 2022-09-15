from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def monthly_challanges_by_number(request, month):

    months = list(monthly_challangess.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    return HttpResponseRedirect(redirect_month)


def monthly_challanges(request, month):
    try:
        challange_text = monthly_challangess[month]
        return HttpResponse(challange_text)
    except:
        return HttpResponseNotFound("this month does not match!")
