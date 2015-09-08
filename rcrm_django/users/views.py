from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse


@login_required(login_url='/auth/login')
def list_users(request):
    args = {}
    args['list_users'] = auth.models.User.objects.all().order_by('id')
    if "only_table" in request.POST and request.POST['only_table'] == "true":
        return render_to_response('users_only_table.html', args)
    args['username'] = auth.get_user(request).username
    return render_to_response('users.html', args)

@login_required(login_url='/auth/login')
def add_user(request):
    if request.method == 'POST':
        login = request.POST['login']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        passwd = request.POST['pass']
        new_user = auth.models.User.objects.create_user(username=login, email=mail, first_name=fname, last_name=lname, password=passwd)
        q = new_user.save()
        ans = "Request was completed with the code %s." % (q)
        return HttpResponse(ans)
    return HttpResponse("No data in request.")

@login_required(login_url='/auth/login')
def rem_user(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        user_to_remove = auth.models.User.objects.get(id=user_id)
        user_to_remove.is_active = False
        q = user_to_remove.save()
        ans = "Request was completed with the code %s." % (q)
        return HttpResponse(ans)
    return HttpResponse("No data in request.")

@login_required(login_url='/auth/login')
def check_login(request):
    if request.method == 'POST':
        login = request.POST['login']
        user = False
        try:
            user = auth.models.User.objects.get(username=login)
        except:
            pass
        if user:
            return HttpResponse("Имя занято!!!")
    return HttpResponse("Имя свободно")
