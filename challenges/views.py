from django.http import Http404, HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
  "January": "30-day coding challenge: Build one small project every day",
  "February": "Learn a new programming language basics in 28 days",
  "March": "Contribute to 5 open source projects",
  "April": "Create and deploy a full-stack web application",
  "May": "Complete 50 LeetCode problems",
  "June": "Build a mobile app using Flutter/React Native",
  "July": "Master DevOps tools (Docker, Jenkins, Kubernetes)",
  "August": "Create a personal blog and write 15 technical articles",
  "September": "Build 3 REST APIs with different tech stacks",
  "October": "Implement 10 different design patterns in projects",
  "November": "Create a machine learning project from scratch",
  "December": None,
}
# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect(reverse('month_challenge', args=[redirect_month]))

def monthly_challenge(request, month):
    month = month.capitalize()
    try:
        challenge_text  = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
    