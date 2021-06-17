from django.contrib import admin
from django.urls import path
from app.views import location, set_location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', location),
    path('coordinate/', set_location, name = 'set_location'),
]
