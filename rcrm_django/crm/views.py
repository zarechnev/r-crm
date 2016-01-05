from django.shortcuts import render_to_response
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth
import simplejson
from crm.models import Task
from clients.models import Client
import datetime
import time


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
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        current_user = auth.get_user(request)
        request_inn = request.POST['inn']
        comment = request.POST['comment']
        try:
            finded_client = Client.objects.get(inn=request_inn)
            new_task = Task(create_user=current_user, client=finded_client, create_date=timezone.now(), create_comment=comment)
            new_task.set_status("NEW")
            ans = new_task.save()
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)

@login_required(login_url='/auth/login')
def rem_task(request):
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        id_task = request.POST['id']
        task_to_rem = Task.objects.get(id=id_task)
        task_to_rem.date_of_removal = timezone.now()
        try:
            task_to_rem.is_removed = True
            task_to_rem.remove_user = auth.get_user(request)
            ans = task_to_rem.save()
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)

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

@login_required( login_url='/auth/login' )
def task_switch_status( request ):
    MIN_INTERVAL_CHANGE_STATUS = 10
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        id_task = request.POST['id']
        task_status = request.POST['status']
        task_to_change = Task.objects.get( id = id_task )

        delta_sec = timezone.now() - task_to_change.change_status_datetime
        delta_sec = int( delta_sec.total_seconds() )

        if ( delta_sec <= MIN_INTERVAL_CHANGE_STATUS ):
            return HttpResponse( "После прошлого изменения статуса прошло менее %s секунд: %s секунд(ы)!" % ( MIN_INTERVAL_CHANGE_STATUS, delta_sec ) )

        try:
            task_to_change.set_status( task_status )
            if ( task_status == "PRG" ):
                task_to_change.solves_user = auth.get_user(request)
            if ( task_status == "SLD" ):
                task_to_change.user_solved = auth.get_user(request)

            task_to_change.change_status_datetime = timezone.now()

            ans = task_to_change.save()
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)