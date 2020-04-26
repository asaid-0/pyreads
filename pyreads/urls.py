"""pyreads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from register.views import register, activate
from users.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('home/', include('users.urls')),
    path('home/', include('projects.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/',register,name='register'),
    path('accounts/',include('allauth.urls')),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)