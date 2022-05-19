from categories.models import Category
from django.http import HttpResponse
from django.shortcuts import render
from news.models import News


def show_home(request):
    # https://www.codegrepper.com/
    categories = Category.objects.all()
    business_news = News.objects.filter(category_id=2).order_by('-id')[:4]
    return render(request, 'index.html', {'categories': categories, 'business_news': business_news})


def show_about(request):
    return render(request, 'test.html')


def show_contacts(request):
    return HttpResponse('Contacts')

