from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth
from django.utils import timezone
from chat.models import Chat


@login_required()
def show_chat(request):
    args = {}
    args['messages'] = Chat.objects.all().order_by('id').reverse()[:5]
    return render_to_response('chat.html', args)


@login_required()
def add_post(request):
    if request.method == 'POST':
        current_user = auth.get_user(request)
        message = request.POST['message']
        if not message:
            return HttpResponse("Message is empty.")
        new_message = Chat(create_post_user=current_user, post_date=timezone.now(), post_text=message)
        q = new_message.save()
        ans = "Request was completed with the code %s." % q
        return HttpResponse(ans)
    return HttpResponse("No data in request.")
