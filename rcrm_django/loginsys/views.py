from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf


def login(request):
    if request.user.is_authenticated():
        return redirect('/crm')
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if (user is not None) and user.is_active:
            auth.login(request, user)
            # TODO: Реализовать перенаправление на запрашиваемую страницу
            return redirect('/crm')
        else:
            args['login_error'] = "Проверьте правильность введённых данных."
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return render_to_response('login.html')
