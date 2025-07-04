from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from courses.models import Course


@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except Course.DoesNotExist:
        return HttpResponseForbidden()
    # retrive chat history
    latest_messages = course.chat_messages.select_related(
        'user'
    ).order_by('-id')[0:5]
    latest_messages = reversed(latest_messages)
    return render(
        request,
        template_name='chat/room.html',
        context={
            'course': course,
            'latest_messages': latest_messages
        }
    )
