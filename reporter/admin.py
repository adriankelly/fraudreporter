from django.contrib import admin

# Register your models here.
from .models import Case, Report, Author

admin.site.register(Case)
admin.site.register(Report)
admin.site.register(Author)