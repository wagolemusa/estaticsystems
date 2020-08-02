from django.urls import path
from django.conf.urls import  url

from .views import(
	home,
	about,
	contact
)

app_name = 'systems'
urlpatterns = [

	path('', home, name='home'),
	path('about/', about, name='about'),
	
]