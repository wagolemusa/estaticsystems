from django.db import models
# Create your models here.
from django.conf import settings
from django.shortcuts import reverse

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Category(models.Model):
	name = models.CharField(max_length=250)


	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_category_absolete_url(self):
		return reverse('systems:list_category',	args=[self.id])

	def __str__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE,
										related_name="category_set")
	content = models.TextField()
	image = models.ImageField(upload_to="upload_location",
		null=True,
		blank=True,
		width_field="width_field",
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field  = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse("systems:show", kwargs={"id": self.id })

class Postjob(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email = models.CharField(max_length=250)
	company = models.CharField(max_length=200)
	phone = models.BigIntegerField(blank=True, null=True)
	content = models.TextField()

	def __str__(self):
		return self.firstname

class Contact(models.Model):
	full_name = models.CharField(max_length=120)
	phone  = models.IntegerField()
	email = models.CharField(max_length=150)
	subject = models.CharField(max_length=200)
	message = models.TextField(max_length=500)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.full_name

	def __str__(self):
		return self.full_name