from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),
    path('', include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Customizing admin area

## Change title from 'Django administration' to 'CM Administration'
admin.site.site_header = 'CM Administration'	

## Change sub-title from 'Site administration' to 'Welcome to project'
admin.site.index_title = 'Welcome to project'

## Change browser title from 'Welcome to project | Django site' to 'Welcome to project | Control Panel'
admin.site.site_title = 'Control Panel'