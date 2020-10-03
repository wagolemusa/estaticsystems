from django.urls import path
from django.conf.urls import  url

from .views import(
	home,
	post,
	job,
	about,
	contact,
	services,
	work,
	show,

)

app_name = 'systems'
urlpatterns = [

	path('', home, name='home'),
	path('<int:id>/', show, name='show'),
	path('post/', post, name='post'),
	path('job/', job, name='job'),
	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('services/', services, name='services'),
	path('work/', work, name='work')
	
	
	
]