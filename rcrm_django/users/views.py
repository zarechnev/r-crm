from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
import simplejson


@login_required(login_url='/auth/login')
def list_users(request):
    args = {'type': "main"}
    language = get_language()
    args['language'] = language
    users_list = auth.models.User.objects.all().order_by('-is_active', 'id')

    count = auth.models.User.objects.all().count()
    args['users_count'] = count

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
    ans = _("No data in request")
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
    ans = _("No data in request")
    if request.method == 'POST':
        login = request.POST['login']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        passwd = request.POST['pass']
        try:
            new_user = auth.models.User.objects.create_user(username=login, email=mail, first_name=fname,
                                                            last_name=lname)
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
            return HttpResponse(_("Login currently in use"))
    return HttpResponse(_("Login is free"))


@login_required(login_url='/auth/login')
def user_switch_status(request):
    ans = _("No data in request")
    if request.method == 'POST':
        try:
            user_id = request.POST['id']
            user_status = request.POST['status']
            user_to_switch_status = auth.models.User.objects.get(id=user_id)
            if user_status == '1':
                user_to_switch_status.is_active = 1
            elif user_status == '0':
                user_to_switch_status.is_active = 0
            else:
                ans = _("Status is undefined")
                return HttpResponse(ans)
            ans = user_to_switch_status.save()
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)


@login_required(login_url='/auth/login')
def find_user(request):
    args = {'type': "find"}
    ans = _("No data in request")
    users_list = []
    if request.method == 'POST':
        user_name = request.POST['find_user_name']
        for user in auth.models.User.objects.all():
            if user_name.upper() in user.last_name.upper():
                users_list.append(user)
        if not users_list:
            return HttpResponse(_("No users found"))
        args['users'] = users_list
        return render_to_response('users_only_table.html', args)
    return HttpResponse(ans)


@login_required(login_url='/auth/login')
def auto_complete_solves_user(request):
    tags = []
    i = 0
    if 'term' in request.GET:
        for user_i in auth.models.User.objects.all():
            if request.GET['term'].upper() in user_i.last_name.upper():
                addstring = "%s (%s %s)" % (user_i.username, user_i.last_name, user_i.first_name)
                tags.append(addstring)
                if i > 3:
                    return HttpResponse(simplejson.dumps(tags))
                i += 1
    return HttpResponse(simplejson.dumps(tags))
