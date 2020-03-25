from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/<str:id>', core_views.get_pixel, name='get-pixel'),
]

admin.site.site_header = 'Dashboard | TraceThePixel'
admin.site.site_title = 'TraceThePixel'
