# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact

# Customizing Contacts table
class ContactAdmin(admin.ModelAdmin):
	list_display  = ('name', 'gender', 'email', 'info', 'phone', 'date_added')
	list_editable = ('info', 'phone',)
	list_per_page = 1
	search_fields = ('name', 'gender', 'email', 'info', 'phone')
	list_filter   = ('gender', 'date_added')

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)

