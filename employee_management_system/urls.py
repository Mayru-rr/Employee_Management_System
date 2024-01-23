from django.contrib import admin
from django.urls import include, path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path('employee/', include('employee_management.urls')),
    
]
