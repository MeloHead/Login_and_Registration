from django.urls import path
from . import views

urlpatterns = [
    #render route
    path('', views.registration_page), #index
    path('registration_success', views.registration_success),
    path('login_success', views.login_success),
    # path('fail', views.login_success),
    
    #action route
    path('registration_process', views.registration_process),
    path('login_process', views.login_process),
    path('logout', views.logout)
]


