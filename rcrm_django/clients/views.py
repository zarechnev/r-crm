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
def add_client(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        fname = request.POST['fname']
        inn = request.POST['inn']
        address = request.POST['address']
        phone = request.POST['phone']
        priority = request.POST['priority']
        mail = request.POST['mail']
        new_client = Client(sname=sname, name=fname, inn=inn, phone=phone, address=address, priority=priority, email=mail, is_enabled=True, create_date=datetime.now())
        q = new_client.save()
        ans = "Request was completed with the code %s." % (q)
        return HttpResponse(ans)
    return HttpResponse("No data in request.")

@login_required(login_url='/auth/login')
def rem_client(request):
    if request.method == 'POST':
        client_id = request.POST['id']
        client_to_remove = Client.objects.get(id=client_id)
        client_to_remove.is_deleted = True
        q = client_to_remove.save()
        ans = "Request was completed with the code %s." % (q)
        return HttpResponse(ans)
    return HttpResponse("No data in request.")