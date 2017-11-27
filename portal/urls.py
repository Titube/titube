from django.conf.urls import url
from portal.views import home

urlpatterns = [
	url(r'^$', home),
]