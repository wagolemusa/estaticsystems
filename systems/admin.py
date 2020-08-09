from django.contrib import admin

# Register your models here.
from .models import Post, Postjob, Contact, Category

admin.site.register(Post)
admin.site.register(Postjob)
admin.site.register(Contact)
admin.site.register(Category)
