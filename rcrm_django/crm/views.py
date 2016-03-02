from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth
import simplejson
from crm.models import Task
from clients.models import Client


@login_required(login_url='/auth/login')
def hello(request):
    args = {}
    tasks_list = Task.objects.all().order_by('-id')

    if "only_my_tasks" in request.COOKIES and request.COOKIES['only_my_tasks'] == str(1):
        current_user = auth.get_user(request)
        tasks_list = tasks_list.filter(solves_user=current_user)
        args['only_my_tasks'] = True
    else:
        args['only_my_tasks'] = False

    if "hide_deleted_tasks" in request.COOKIES and request.COOKIES['hide_deleted_tasks'] == str(1):
        tasks_list = tasks_list.exclude(is_removed='True').exclude(status='SLD')
        args['hide_deleted_tasks'] = True
    else:
        args['hide_deleted_tasks'] = False

    objects_on_list = 7
    paginator = Paginator(tasks_list, objects_on_list)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tasks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tasks = paginator.page(paginator.num_pages)
    args['tasks'] = tasks
    args['statuses'] = Task.PRIO_OF_TASK_TEMPLATE
    if "only_table" in request.POST and request.POST['only_table'] == "true":
        return render_to_response('crm_only_table.html', args)

    args['username'] = auth.get_user(request).username
    return render_to_response('crm.html', args)


@login_required(login_url='/auth/login')
def add_task(request):
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        current_user = auth.get_user(request)
        request_inn = request.POST['inn'].split(" ")[0]
        comment = request.POST['comment']
        solves_user = request.POST['ingener'] or None
        prio = request.POST['priority'] or None
        try:
            finded_client = Client.objects.get(inn=request_inn)
            new_task = Task(create_user=current_user, client=finded_client, create_date=timezone.now(),
                            create_comment=comment, solves_user=solves_user)
            new_task.set_status("NEW")
            new_task.set_prio(prio)
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
                    return HttpResponse(simplejson.dumps(tags))
                i += 1
    return HttpResponse(simplejson.dumps(tags))


@login_required(login_url='/auth/login')
def task_switch_status(request):
    # Интервал задержки смены статуса
    min_interval = 5
    ans = "Нет данных в запросе"
    if request.method == 'POST':
        id_task = request.POST['id']
        task_status = request.POST['status']
        task_to_change = Task.objects.get(id=id_task)

        if task_to_change.is_removed:
            return HttpResponse("Task already been removed.")

        if task_to_change.status == task_status:
            return HttpResponse("Статус уже %s!" % task_to_change.status_to_template())

        if task_to_change.change_status_datetime:
            delta_sec = timezone.now() - task_to_change.change_status_datetime
            delta_sec = int(delta_sec.total_seconds())

            if delta_sec < min_interval:
                msg = "После прошлого изменения статуса прошло менее %s секунд: %s секунд(ы)!" % (
                    min_interval, delta_sec)
                return HttpResponse(msg)

        try:
            if task_status == "NEW":
                task_to_change.solves_user = None
                task_to_change.user_solved = None
            if task_status == "PRG":
                task_to_change.solves_user = auth.get_user(request)
                task_to_change.user_solved = None
            if task_status == "SLD":
                task_to_change.user_solved = auth.get_user(request)
                if not task_to_change.solves_user:
                    task_to_change.solves_user = auth.get_user(request)

            task_to_change.set_status(task_status)
            task_to_change.change_status_datetime = timezone.now()

            ans = task_to_change.save()
        except BaseException as e:
            ans = str(e)
    return HttpResponse(ans)


@login_required(login_url='/auth/login')
def hide_closed_tasks(request):
    response = HttpResponse(request.POST['hide_closed_tasks'])
    if "hide_closed_tasks" in request.POST:
        response.set_cookie("hide_deleted_tasks", request.POST['hide_closed_tasks'])
    else:
        response.set_cookie("hide_deleted_tasks", 0)
    return response


@login_required(login_url='/auth/login')
def only_my_tasks(request):
    response = HttpResponse(request.POST['only_my_tasks'])
    if "only_my_tasks" in request.POST:
        response.set_cookie("only_my_tasks", request.POST['only_my_tasks'])
    else:
        response.set_cookie("only_my_tasks", 0)
    return response
