
from django.contrib import admin
from django.urls import path,include
from akhbar.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('views/',include("akhbar.urls")),
   # path('views/',khabar),
]
