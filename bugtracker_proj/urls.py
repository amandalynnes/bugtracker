"""bugtracker_proj URL Configuration

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
from django.urls import path
from bugtracker_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('addticket/', views.add_ticket, name='add_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_view, name='ticket'),
    path('ticket/edit/<int:ticket_id>/', views.ticket_edit, name='edit_ticket'),
    path('author/edit/<int:author_id>/', views.author_edit, name='edit_author'),
    path('author/<int:author_id>/', views.author_view, name='author_view'),


]
