"""angular_tour_of_heroes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.views import serve
from django.views.decorators.csrf import csrf_exempt

from heroes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/heroes/<pk>', views.hero_detail.as_view()),
    path('static/<path>', RedirectView.as_view(url='/static/frontend/%(path)s', permanent=False)),
    path('api/heroes/', views.hero_list.as_view()),
    path('rest-auth/', include('rest_auth.urls')),  # auth
    # path('accounts/', include('django.contrib.auth.urls')),  # auth

]
