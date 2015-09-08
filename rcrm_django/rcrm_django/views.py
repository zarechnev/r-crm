from django.shortcuts import render_to_response
from django.contrib import auth


def index(request):
    args = {}
    args['username'] = auth.get_user(request).username
    return render_to_response('main-page.html', args)
