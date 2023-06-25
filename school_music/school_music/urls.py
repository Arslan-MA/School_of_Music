"""
URL configuration for school_music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school_app.views import admin_page, student_data, adding_students, student_editing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_page, name='admin_page'),
    path('studentData/', student_data, name='data'),
    path('addingStudents/', adding_students, name='add'),
    path('studentEditing/<int:student>', student_editing, name='update')
]
