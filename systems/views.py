from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator 
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Postjob, Contact, Category
from .forms import PostForm, PostjobForm, CantactForms

def home(request):
	object_list = Post.objects.all().order_by("-timestamp")[:4]

	context = {
		'object_list' : object_list,
	}
	return render(request, "home.html", context)

def post(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")

	content = {
		'form': form,
	}
	return render(request, "post.html", content)

def job(request):
	form = PostjobForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Posted Successfully")
		# return HttpResponseRedirect(instance.get_absolute_url())
	content = {
		'form' : form,
	}
	return render(request, "job.html", content)

def about(request):
	return render(request, "about.html")

def contact(request):
	form = CantactForms(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Thanks to reach for us, You get feedback on Email")
	content = {
		'form' : form
	}
	return render(request, "contact.html", content)

def services(request):
	return render(request, "services.html")

def work(request):
	object_list = Post.objects.all().order_by("-timestamp")

	context = {
		'object_list' : object_list,
	}
	return render(request, "work.html", context)

def show(request, id=None):
	instance = get_object_or_404(Post, id=id)
	# qureyset_list = Post.objects.order_by("-timestamp")
	# object_list = Post.objects.all()

	# category = get_object_or_404(Category, slug=slug)

	# show = get_object_or_404(Post, category = id)
	# category = Category.objects.get(id=id)
	# show = Post.objects.filter(category=category)

	qureyset_list = Post.objects.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		qureyset_list = Post.objects.all()
		
	paginator = Paginator(qureyset_list, 3)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	content = {
	'instance': instance,
	"object_list": querySet
	# "show":show
	}
	return render(request, "show.html", content)