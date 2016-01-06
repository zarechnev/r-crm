from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
import logging


@login_required(login_url='/auth/login')
def list_users(request):
    args = {}
    users_list = auth.models.User.objects.all().order_by('-is_active', 'id')
    objects_on_list = 30
    paginator = Paginator(users_list, objects_on_list)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)
    args['users'] = users
    if "only_table" in request.POST and request.POST['only_table'] == "true":
        return render_to_response('users_only_table.html', args)
    args['username'] = auth.get_user(request).username
    return render_to_response('users.html', args)

@login_required(login_url='/auth/login')
def edit_user(request):
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        login = request.POST['login']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        passwd = request.POST['pass']
        user_to_edit = auth.models.User.objects.get(username=login)
        try:
            user_to_edit.email = mail
            user_to_edit.first_name = fname
            user_to_edit.last_name = lname
            if (passwd):
                user_to_edit.set_password(passwd)
            ans = str(user_to_edit.save())
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)

@login_required(login_url='/auth/login')
def add_user(request):
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        login = request.POST['login']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        passwd = request.POST['pass']
        try:
            new_user = auth.models.User.objects.create_user(username=login, email=mail, first_name=fname, last_name=lname)
            new_user.set_password(passwd)
            ans = str(new_user.save())
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)

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

@login_required(login_url='/auth/login')
def user_switch_status(request):
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        try:
            user_id = request.POST['id']
            user_status = request.POST['status']
            user_to_switch_status = auth.models.User.objects.get( id = user_id )
            if user_status == '1':
                user_to_switch_status.is_active = 1
            elif user_status == '0':
                user_to_switch_status.is_active = 0
            else:
                ans = "Статус не определён"
                return HttpResponse( ans )
            ans = user_to_switch_status.save()
        except  BaseException as e:
            ans = str( e )
    return HttpResponse( ans )