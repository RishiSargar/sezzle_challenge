from django.shortcuts import render


def index(request):
    return render(request, 'Calculator_App/index.html', {})


def session(request, session_name):
    return render(request, 'Calculator_App/session.html', {
        'session_name': session_name
    })