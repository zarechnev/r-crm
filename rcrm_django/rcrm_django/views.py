from django.utils.translation import get_language
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib import auth


@login_required(login_url='/auth/login')
def index(request):
    args = {'username': auth.get_user(request).username}
    language = get_language()
    args['language'] = language
    return render_to_response('help-page.html', args)
