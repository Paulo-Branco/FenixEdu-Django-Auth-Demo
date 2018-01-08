from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

from demo_app.auth import fenixedu_client


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponse('Logged in as {} ({})!'.format(request.user.first_name, request.user.username))
    else:
        return HttpResponseRedirect(fenixedu_client.get_authentication_url())


def handle_fenix_auth(request):
    code = request.GET.get('code', None)
    if code is not None and not request.user.is_authenticated():
        user = authenticate(request=request, client=fenixedu_client, code=code)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    return HttpResponse('An error occured while trying to authenticate you with FenixEdu', status=500)
