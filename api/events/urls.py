"""CrowdAlert Web  URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from api.events import views

urlpatterns = [
    # API paths
    path('view/', views.home, name='home'),
    path('geteventbyid', views.get_event_by_id, name='get event by id'),
    path('geteventsbylocation', views.get_events_by_location,
     name='get events by a location & thresold'),
]