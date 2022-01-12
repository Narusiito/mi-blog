from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/', views.pages, name='pages'),
    path('page/<str:id>/', views.page, name='page'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),

]