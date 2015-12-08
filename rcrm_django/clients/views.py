from django.shortcuts import render_to_response
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib import auth
from clients.models import Client


@login_required(login_url='/auth/login')
def hello(request):
    args = {}
    args['clients'] = Client.objects.all
    if "only_table" in request.POST and request.POST['only_table'] == "true":
        return render_to_response('clients_only_table.html', args)

    args['username'] = auth.get_user(request).username
    return render_to_response('clients.html', args)

#TODO: Заменить эту порнографию на передачу json-объекта.
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
    ans = "Нет данных в запросе"
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
            # Пользователь существует
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
            # Пользователь не существует
            try:
                new_client = Client(sname=sname, name=fname, inn=inn, phone=phone, address=address, priority=priority, email=mail, is_enabled=True, create_date=datetime.now())
                ans = new_client.save()
            except BaseException as e:
                ans = str(e)
    return HttpResponse(ans)

@login_required(login_url='/auth/login')
def rem_client(request):
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        try:
            client_id = request.POST['id']
            client_to_remove = Client.objects.get(id=client_id)
            client_to_remove.is_deleted = True
            ans = client_to_remove.save()
        except  BaseException as e:
            ans = str(e)
    return HttpResponse(ans)

@login_required(login_url='/auth/login')
def client_switch_status(request):
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        try:
            client_id = request.POST['id']
            client_status = request.POST['status']
            client_to_switch_status = Client.objects.get(id=client_id)
            client_to_switch_status.is_enabled = client_status
            ans = client_to_switch_status.save()
        except  BaseException as e:
            ans = str(e)
    return HttpResponse(ans)