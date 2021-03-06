from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from clients.models import Client


@login_required(login_url='/auth/login')
def hello(request):
    args = {'type': "main", 'client_obj': Client}
    language = get_language()
    args['language'] = language
    clients_list = Client.objects.all().order_by('-is_active', 'id')

    count = Client.objects.all().count()
    args['clients_count'] = count

    objects_on_list = 30
    paginator = Paginator(clients_list, objects_on_list)
    page = request.GET.get('page')
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clients = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clients = paginator.page(paginator.num_pages)
    args['clients'] = clients
    if "only_table" in request.POST and request.POST['only_table'] == "true":
        return render_to_response('clients_only_table.html', args)

    args['username'] = auth.get_user(request).username
    return render_to_response('clients.html', args)


# TODO: Replace with json-object sending
@login_required(login_url='/auth/login')
def get_client_info(request, id):
    obj = Client.objects.get(id=id)
    field = request.POST['field']
    ans = ""
    if field == "name":
        ans = obj.name
    elif field == "sname":
        ans = obj.sname
    elif field == "inn":
        ans = obj.inn
    elif field == "address":
        ans = obj.address
    elif field == "phone":
        ans = obj.phone
    elif field == "email":
        ans = obj.email
    elif field == "priority":
        ans = obj.priority
    return HttpResponse(ans)


@login_required(login_url='/auth/login')
def add_edit_client(request):
    ans = _("No data in request")
    if request.method == 'POST':
        sname = request.POST['sname']
        fname = request.POST['fname']
        inn = request.POST['inn']
        address = request.POST['address']
        phone = request.POST['phone']
        priority = request.POST['priority']
        mail = request.POST['mail']
        try:
            existing_client = Client.objects.get(sname=sname)
        except:
            existing_client = 0
        if existing_client:
            # User is exist
            try:
                existing_client.name = fname
                existing_client.inn = inn
                existing_client.phone = phone
                existing_client.address = address
                existing_client.priority = priority
                existing_client.email = mail
                ans = existing_client.save()
            except BaseException as e:
                ans = str(e)
        else:
            # User does not exist
            try:
                new_client = Client(sname=sname, name=fname, inn=inn, phone=phone, address=address, priority=priority,
                                    email=mail, create_date=timezone.now())
                ans = new_client.save()
            except BaseException as e:
                ans = str(e)
    return HttpResponse(ans)


@login_required(login_url='/auth/login')
def rem_client(request):
    ans = _("No data in request")
    if request.method == 'POST':
        try:
            client_id = request.POST['id']
            client_to_remove = Client.objects.get(id=client_id)
            client_to_remove.is_deleted = True
            ans = client_to_remove.save()
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)


@login_required(login_url='/auth/login')
def client_switch_status(request):
    ans = _("No data in request")
    if request.method == 'POST':
        try:
            client_id = request.POST['id']
            client_status = request.POST['status']
            client_to_switch_status = Client.objects.get(id=client_id)
            if client_status == "1":
                client_to_switch_status.is_active = 1
            elif client_status == "0":
                client_to_switch_status.is_active = 0
            else:
                ans = _("Status is undefined")
                return HttpResponse(ans)
            ans = client_to_switch_status.save()
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)


@login_required(login_url='/auth/login')
def find_client(request):
    args = {'type': "find", 'client_obj': Client}
    ans = _("No data in request")
    client_list = []
    if request.method == 'POST':
        client_name = request.POST['find_client']
        for client in Client.objects.all():
            if client_name.upper() in client.name.upper():
                client_list.append(client)
        if not client_list:
            return HttpResponse(_("No client was found"))
        args['clients'] = client_list
        return render_to_response('clients_only_table.html', args)
    return HttpResponse(ans)
