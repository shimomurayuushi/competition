from django.contrib import admin

from compe.models import Category, Problem, Choice

# Register your models here.
admin.site.register(Category)
admin.site.register(Problem)
admin.site.register(Choice)