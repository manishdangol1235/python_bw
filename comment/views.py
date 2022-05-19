from django.http import HttpResponse
from django.shortcuts import render


def post_comment(request):
    return HttpResponse('Post Comment')
