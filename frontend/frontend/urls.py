"""frontend URL Configuration

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
from django.contrib import admin
from django.urls import include, path

from users import views

# Make sure to include url views to the other parts of my site
urlpatterns = [
    # Admin site nice for models
    path('admin/', admin.site.urls),
    # For the no slash, I just put the users index file to be first
    path('', views.index, name='index'),
    # import all the urls for application and user apps
    path('application/', include(('application.urls', 'application'), namespace='application')),
    path('users/', include(('users.urls', 'users'),namespace='users')),
]
