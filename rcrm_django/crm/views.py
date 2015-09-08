from django.shortcuts import render_to_response
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth
from django.utils import simplejson
from crm.models import Task
from clients.models import Client


@login_required(login_url='/auth/login')
def hello(request):
    args = {}
    args['tasks'] = Task.objects.all().order_by('id').reverse()
    if "only_table" in request.POST and request.POST['only_table'] == "true":
        return render_to_response('crm_only_table.html', args)

    args['username'] = auth.get_user(request).username
    return render_to_response('crm.html', args)

@login_required(login_url='/auth/login')
def add_task(request):
    if request.method == 'POST':
        current_user = auth.get_user(request)
        request_inn = request.POST['inn']
        comment = request.POST['comment']
        finded_client = Client.objects.get(inn=request_inn)
        new_task = Task(create_user=current_user, client=finded_client, create_date=datetime.now(), create_comment=comment)
        q = new_task.save()
        ans = "Request was completed with the code %s." % (q)
        return HttpResponse(ans)
    return HttpResponse("No data in request.")

@login_required(login_url='/auth/login')
def rem_task(request):
    if request.method == 'POST':
        id_task = request.POST['id']
        task_to_rem = Task.objects.get(id=id_task)
        task_to_rem.date_of_removal = datetime.now()
        task_to_rem.is_removed = True
        task_to_rem.remove_user = auth.get_user(request)
        q = task_to_rem.save()
        ans = "Request was completed with the code %s." % (q)
        return HttpResponse(ans)
    return HttpResponse("No data in request.")

@login_required(login_url='/auth/login')
def auto_complite_inn(request):
    tags = []
    i = 0
    if 'term' in request.GET:
        for client_i in Client.objects.all():
            if request.GET['term'] in client_i.inn:
                addstring = "%s (%s)" % (client_i.inn, client_i.sname)
                tags.append(addstring)
                if i > 3:
                    return HttpResponse( simplejson.dumps( tags ) )
                i = i + 1
    return HttpResponse( simplejson.dumps( tags ) )