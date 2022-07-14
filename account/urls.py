
from django.urls import path,include
from account import views

urlpatterns = [
    path('signup/', views.UserRegistrationView, name='signup'),
    path('signin/', views.UserLoginView, name='signIn'),

    #path('getnotes/', views.getNotes, name='getNotes'),

]
