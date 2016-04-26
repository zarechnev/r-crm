from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib import auth


@login_required(login_url='/auth/login')
def index(request):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
    return render_to_response('help-page.html', args)
