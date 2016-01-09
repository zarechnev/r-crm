from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth


@login_required(login_url='/auth/login')
def hello(request):
    args = {}
    args['username'] = auth.get_user(request).username
    return render_to_response('statistic.html', args)


@login_required(login_url='/auth/login')
def tasks(request):
    pass


@login_required(login_url='/auth/login')
def clients(request):
    pass


@login_required(login_url='/auth/login')
def users(request):
    pass
