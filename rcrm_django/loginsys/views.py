from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf


def login(request):
    if request.user.is_authenticated():
        return redirect('/crm')
    language = get_language()
    args = {'language': language}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if (user is not None) and user.is_active:
            auth.login(request, user)
            return redirect('/crm')
        else:
            args['login_error'] = _("Cheek login and password")
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')
