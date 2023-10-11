from django.urls import path, include
#from django.contrib.auth import views as auth_views

from . import views
#from .forms import LoginForm

app_name = 'core'

urlpatterns = [
	# path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),

	path('api/change_dark_mode/', views.api_change_dark_mode),
]