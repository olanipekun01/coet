from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404
from django.shortcuts import render

# Define the custom 404 view
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# Set the handler for 404 errors
handler404 = custom_404_view


app_name = "app"

urlpatterns = [
    path('', views.Index, name="index"),
    path('about/', views.About, name="about"),
    path('principalofficers/', views.PrincipalOfficers, name="principalofficers"),
    path('admissions/', views.Amissions, name="admissions"),
    path('staff/', views.Staff, name="staff"),
    path('contact/', views.Contact, name="contact"),
    path('departments/', views.Department, name="department"),
    path('dept/<str:pk>', views.EachDepartment, name="eachdepartment"),
    path('accounts/login/', views.Login, name="login"),
    path('accounts/signup/', views.Signup, name="signup"),

    # path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),
    # path('accounts/login/', views.login_view, name="login_view"),
    # path('accounts/logout/', views.logout, name="logout"),


   

    # path('404', views.F404, name='f404')
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

# if settings.DEBUG is False:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)