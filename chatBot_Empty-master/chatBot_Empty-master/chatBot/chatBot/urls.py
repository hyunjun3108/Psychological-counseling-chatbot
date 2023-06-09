"""
URL configuration for chatBot project.

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
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('startPage.html', include('startPage.urls')),
    path('', RedirectView.as_view(url="/startPage.html", permanent=True)), #서버 접속시 startPage.html로 시작하게끔
    path('introPage.html', include('introPage.urls')),
    path('loginPage.html', include('loginPage.urls')),
    path('mainPage.html', include('mainPage.urls')),
    path('joinPage.html', include('joinPage.urls')),
]
