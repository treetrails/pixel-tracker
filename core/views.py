# from django.http.response import HttpResponse
# from django.conf import settings
# import os
from django.shortcuts import redirect
from core.models import Target, Activity


def get_pixel(request, id):
    """
    get ID from URL, fetch TARGET object for that ID REDIRECT to the target object's redirect_uri
    """
    try:
        target = Target.objects.get(id=id)
        redirect_uri = target.redirect_uri
        data = request.META
        activity = Activity.objects.create(
            target=target,
            # remote_addr=data.get('REMOTE_ADDR'),
            remote_addr=data.get('HTTP_X_FORWARDED_FOR'),
            user_agent=data.get('HTTP_USER_AGENT')
        )
        print(data)
        print(f'TARGET: {target.__dict__}')
        print(f'ACTIVITY: {activity.__dict__}')
        return redirect(redirect_uri)
    except Exception as e:
        print(f'EXCEPTION: << id {id} >> {str(e)}')
        return redirect('https://www.example.com')
