import fenixedu
from django.core.exceptions import ImproperlyConfigured

from FenixAuthDemo.settings import FENIXEDU_CLIENT_ID, FENIXEDU_REDIRECT_URI, FENIXEDU_CLIENT_SECRET, FENIXEDU_BASE_URL

if FENIXEDU_CLIENT_ID == "" or FENIXEDU_CLIENT_SECRET == "":
    raise ImproperlyConfigured('You need to define the Client ID and Client Secret values in your module\'s settings')

config = fenixedu.FenixEduConfiguration(FENIXEDU_CLIENT_ID, FENIXEDU_REDIRECT_URI, FENIXEDU_CLIENT_SECRET, FENIXEDU_BASE_URL)
fenixedu_client = fenixedu.FenixEduClient(config)