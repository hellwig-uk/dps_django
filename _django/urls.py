"""_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include

from applications.api.views import APIRootIndex
import applications.api.url


urlpatterns = [
    path("_/admin/", admin.site.urls),
    path("api/", APIRootIndex.as_view(patterns=applications.api.url.urlpatterns), name="api"),
    path('api/auth/', include('dj_rest_auth.urls')),    
    path("api/", include((applications.api.url, "applications.api"), "api")),    
]


if settings.DEBUG:
    from applications.api.views import DeveloperServer
    urlpatterns += [
        re_path(r"^.*$", DeveloperServer.as_view(), name='developer_server')
    ]